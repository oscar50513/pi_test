import time
import picamera
import os

if not os.path.exists("img"):
    os.mkdir("img")

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 1280) 
    camera.start_preview()
    time.sleep(1)
    for i, filename in enumerate(camera.capture_continuous('img/image{counter:02d}.jpg')):
        print('Captured image %s' % filename) 
        if i == 10:
            break
        time.sleep(1)
    camera.stop_preview()