import cv2
import os
import numpy as np
import sys

path='/media/dmitry/Ubuntu/python_programs' # sys.argv[1] #'/home/dmitry/Desktop/Untitled Folder 4/python_programs'
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
prev_image = None
EMPTY = np.zeros((480, 720), dtype = np.uint8)
counter = 2
global_counter = 0

for img in sorted(os.listdir(path)):
	if img.endswith("jpg"):
		print(os.path.join(path, img))
		image = cv2.imread(os.path.join(path, img))
		fgmask = fgbg.apply(image)
		fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

		if not np.array_equal(fgmask, EMPTY):
			print('save prev_image, counter = 2')
			counter = 2

		edges = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		edges = cv2.bilateralFilter(edges, 11, 17, 17)
		cv2.imshow("survelliance", fgmask)
		cv2.imshow("origin", image)
		cv2.imshow("edges", edges)

		if counter > 0: counter -= 1
		elif global_counter < 200: pass
		elif prev_image:
			print('removing {}'.format(prev_image))
			os.remove(os.path.join(path, prev_image))
		prev_image = img
		global_counter += 1

		k = cv2.waitKey(4)
		if k == 27:
			break

cv2.destroyAllWindows()
