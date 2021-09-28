import cv2
import imutils

cap = cv2.VideoCapture("rtsp: ")

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_size = (int(width), int(height))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('./data/record1.mp4', fourcc, 20.0, frame_size)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = imutils.resize(frame, width=800)
    out1.write(frame)


    cv2.imshow("RTSP", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
out1.release()
cv2.destroyAllWindows()
