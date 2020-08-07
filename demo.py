import argparse
from Facecv import FaceCV
import cv2
from time import sleep
def get_args():
    parser = argparse.ArgumentParser(description="This script detects faces from web cam input, "
                                                 "and estimates age and gender for the detected faces.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--depth", type=int, default=16,
                        help="depth of network")
    parser.add_argument("--width", type=int, default=8,
                        help="width of network")
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    depth = args.depth
    width = args.width

    face = FaceCV(depth=depth, width=width)

    # 0 means the default video capture device in OS
    video_capture = cv2.VideoCapture(0)
    # infinite loop, break by key ESC
    while True:
        if not video_capture.isOpened(): 
            sleep(5)
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        outimg,ages,genders = face.detect_and_predict(frame)
        cv2.imshow('Keras Faces', outimg)
        if cv2.waitKey(5) == 27:  # ESC key press
            break
        # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()