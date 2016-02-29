import cv2
import thinning

img = cv2.imread("./example.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thinned = thinning.guo_hall_thinning(img_gray)
cv2.imwrite("./thinned.png", thinned)