from PIL import Image
import pytesseract
import cv2
import re
import pprint
from solver import WordSearchSolver

# img = Image.open("word_search_edit.png", 0)
# string = pytesseract.image_to_string(image, lang="eng")

img = cv2.imread("bank.jpg")
# blurred = cv2.pyrMeanShiftFiltering(img, 200, 200)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# blur = cv2.medianBlur(gray,5)
blur = cv2.GaussianBlur(gray,(5,5),0)
# ret3,threshed = cv2.threshold(blur,0,400,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# _, contours,_ = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(img, contours, 0, (0,0,255), 6)
threshed = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
# outer_box = Mat(sudoku.size(), CV_8UC1);
# ret,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# threshed = cv2.GaussianBlur(threshed,(3,3),0)

#
# ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("mkm", threshed)
cv2.waitKey(0)

string = pytesseract.image_to_string(gray)
print(string)
# chars = [list(re.sub("0", "o", re.sub("\s","",i))) for i in string.splitlines() if i]
# solver = WordSearchSolver(chars, ["glitter", "blackboard", "homework", "glue  stick", "markers", "stick", "compass"])
# pprint.pprint(solver.solve())


