import cv2
import imutils

url1 = 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'
url2 = 'rtsp://admin:intuintu1!@192.168.0.32:554/profile2/media.smp'
cap = cv2.VideoCapture(url1)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_size = (int(width), int(height))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('record1.mp4', fourcc, 20.0, frame_size)

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
