from threading import Thread
import cv2


class RTSPVideoWriterObject(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))

        self.codec = cv2.VideoWriter_fourcc(*'MPEG')
        self.output_video = cv2.VideoWriter('output.avi', self.codec, 30, (self.frame_width, self.frame_height))

        # 프레임을 처리, 저장하는데 중점을 둔 별도의 스레드
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def show_frame(self):

        if self.status:
            cv2.imshow('frame', self.frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            self.output_video.release()
            cv2.destroyAllWindows()
            exit(1)

    def save_frame(self):
        self.output_video.write(self.frame)


if __name__ == '__main__':
    url1 = 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'
    rtsp_stream_link = 'rtsp://admin:test@192.168.0.1/profile2/media.smp'
    video_stream_widget = RTSPVideoWriterObject(url1)
    while True:
        try:
            video_stream_widget.show_frame()
            video_stream_widget.save_frame()
        except AttributeError:
            pass
