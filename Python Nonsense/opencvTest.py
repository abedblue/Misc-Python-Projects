import numpy as np
import cv2

img = cv2.imread('C:\Users\Abe\Pictures\UrealmsSppokyRat.png',-1)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()
