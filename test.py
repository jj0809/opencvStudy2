import cv2
import imutils

cap = cv2.VideoCapture("rtsp: ")

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)


cap.set(cv2.CAP_PROP_FRAME_WIDTH, width/3)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height/3)

while True:
	_, frame = cap.read()
	frame = imutils.resize(frame, width=800)

	cv2.imshow("RTSP", frame)
	k = cv2.waitKey(1)
	if k == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()