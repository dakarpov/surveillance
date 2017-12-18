import picamera
import datetime
import time

camera = picamera.PiCamera()

while True:
	now = datetime.datetime.now()
	filename = "/home/pi/python_programs/img_"+str(now.hour).zfill(2)+str(now.minute).zfill(2)+str(now.second).zfill(2)+".jpg"
	camera.capture(filename)
	time.sleep(5)

