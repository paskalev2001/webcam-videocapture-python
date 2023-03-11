import cv2 as cv

def loopback_camera(src=0, width=640, height=480):
    webcam = cv.VideoCapture(src)
    webcam.set(3, width)
    webcam.set(4, height)

    while webcam.isOpened():
        ret, frame = webcam.read()

        if ret == True:
            cv.imshow("Test Cam - Press 'Q' to close the window", frame )
            key = cv.waitKey(1)
            if key == ord("q"):
                break

    webcam.release()
    cv.destroyAllWindows()


def capture_to_video_file(src=0, path='', width=640, height=480):
    webcam = cv.VideoCapture(src)

    # Define codec & create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(path+'.avi', fourcc, 20.0, (width,  height))

    while webcam.isOpened():
        ret, frame = webcam.read()
        if not ret:
            print("Can't receive frame (stream terminated?)")
            break

        out.write(frame)

        cv.imshow("Recording (" + path + ") - Press 'Q' to stop the recording", frame)
        if cv.waitKey(1) == ord("q"):
            break

    webcam.release()
    out.release()
    cv.destroyAllWindows()
