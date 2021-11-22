import io
import time
import picamera
from base_camera import BaseCamera


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)
            int i = 0
            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()
                with open("test\\" + str(i) + "jpeg", "wb") as file:
                    file.write(stream)
                time.sleep(2)
                i+=1
                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
