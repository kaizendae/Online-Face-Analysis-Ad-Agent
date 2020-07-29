from flask import Flask, render_template, Response, json
from camera import VideoCamera

app = Flask(__name__)

global ages
global genders
info = []

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        global info
        data = camera.get_frame()
        frame = data[0]

        info = []
        info.append(data[1])
        info.append(data[2])

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_info')
def video_info():
    global info
    print('====  ')
    print(info)
    return app.response_class(
        response=json.dumps(info),
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)