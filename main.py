from flask import Flask, render_template, Response, json
import mysql.connector
from mysql.connector import Error
from camera import VideoCamera
import random

app = Flask(__name__)

connection = mysql.connector.connect(host='localhost', database='ads_agent', user='root', password='')

info = []

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        global info
        data = camera.get_frame()
        frame = data[0]
        
        if info != [[], ''] or info == []:
            info = []

            info.append(data[1])
            info.append(data[2])
        else:
            info = [['Loading...'], 'Loading...']

        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
 
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_info')
def video_info():
    global info
    images = []

    if info == [[], '']:
        print("List is empty")
    elif info != []:
        print('====  ')
        print(info)
        try:
            cursor = connection.cursor()
            sql_fetch_images_query = """SELECT image from ads where age = %s and gender = %s"""
            cursor.execute(sql_fetch_images_query, (info[0][0],info[1]))
            record = cursor.fetchall()
            for row in record:
                print("Imaged = ", row[0])
                images.append(row[0])
        except mysql.connector.Error as error:
            print("Failed to read BLOB data from MySQL table {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                print("MySQL connection cursor is closed")
    info.append(images)
    return app.response_class(
        response=json.dumps(info),
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
