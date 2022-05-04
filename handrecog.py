# Recognized Handwritting
# pip install pytesseract
import pytesseract
from PIL import Image
# # Recognize Handwritting
img  = Image.open('hao.jpg')
# text = pytesseract.image_to_string(img)
# print(text)
# Recognize by Language
# pytesseract.image_to_string(img, lang='chi_sim')
# config for Detection
# text = pytesseract.image_to_string(img,  lang='eng',  config='--psm 6')
text = pytesseract.image_to_string(img,  lang='chi_sim',  config='--psm 8')
print(text)
# # Page segmentation modes (--psm num):
#   0    Orientation and script detection (OSD) only.
#   1    Automatic page segmentation with OSD.
#   2    Automatic page segmentation, but no OSD, or OCR.
#   3    Fully automatic page segmentation, but no OSD. (Default)
#   4    Assume a single column of text of variable sizes.
#   5    Assume a single uniform block of vertically aligned text.
#   6    Assume a single uniform block of text.
#   7    Treat the image as a single text line.
#   8    Treat the image as a single word.
#   9    Treat the image as a single word in a circle.
#  10    Treat the image as a single character.
#  11    Sparse text. Find as much text as possible in no particular order.
#  12    Sparse text with OSD.
#  13    Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.


# import cv2
# import pytesseract
#
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
# # Grayscale, Gaussian blur, Otsu's threshold
# image = cv2.imread('1.png')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (3,3), 0)
# thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#
# # Morph open to remove noise and invert image
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
# invert = 255 - opening
#
# # Perform text extraction
# data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
# print(data)
#
# cv2.imshow('thresh', thresh)
# cv2.imshow('opening', opening)
# cv2.imshow('invert', invert)
# cv2.waitKey()


# import pytesseract
# from PIL import Image, ImageEnhance, ImageFilter
#
# im = Image.open("temp.jpg") # the second one
# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.save('temp2.jpg')
# text = pytesseract.image_to_string(Image.open('temp2.jpg'))
# print(text)