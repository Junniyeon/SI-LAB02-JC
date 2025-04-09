import numpy as np
import cv2

img_path = r'C:\Users\DOCENTE\Documents\SI LAB  02\imagen\B.png'
img = cv2.imread(img_path)

width = int(img.shape[1] * 0.3)
height = int(img.shape[0] * 0.3)
dim = (width, height)

resized_img = cv2.resize(img, dim)

cv2.imshow('imagen', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
