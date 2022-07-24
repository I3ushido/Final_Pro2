import pytesseract
import cv2

#im = cv2.imread('info.jpg')
im = cv2.imread('SHK.png')

cv2.imshow('hi',im)
print('OCR : '+pytesseract.image_to_string(im, lang='THA'))



