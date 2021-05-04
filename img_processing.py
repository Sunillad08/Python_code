#from opencv import cv2
import cv2

img1 = cv2.imread("C:\\Users\\DELL\\Desktop\\GIMP Lessons\\Memes\\Meme Template\\0d540e9edbbf70277c8d24766a1e5e86.jpg" , flags = -1)


cv2.imshow("output" , img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

