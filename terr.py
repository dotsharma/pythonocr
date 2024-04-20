# import pytesseract
# from PIL import Image
# import os


# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# os.environ['TESSDATA_PREFIX'] = 'C:\\Program Files\\Tesseract-OCR\\tessdata'

# # Open the image file
# img = Image.open(r"C:\Users\Admin\Downloads\WhatsAppImages.png")

# # Use pytesseract to extract text
# text = pytesseract.image_to_string(img, lang='eng', config='--psm 6 --oem 3')

# # Print the extracted text
# print(text)


# Import the necessary libraries 
import cv2 
import pytesseract 
import numpy as np
 
# If you're on windows, you will need to point pytesseract to the path 
# where you installed Tesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Use OpenCV to read the image 
# replace 'test.png' with your image file 
img = cv2.imread(r"C:\Users\Admin\Downloads\WhatsAppImages.png") 

# Convert the image to gray scale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Use Gaussian blur to remove noise 
blur = cv2.GaussianBlur(gray, (5,5), 0) 

# Use adaptive thresholding to convert the image to binary 
# ADAPTIVE_THRESH_GAUSSIAN_C: threshold value is the weighted sum of 
# neighbourhood values where weights are a gaussian window. 
# BLOCK Size - It decides the size of neighbourhood area. 
# C - It is just a constant which is subtracted from the mean or weighted 
# mean calculated. 
bin_img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
 
# Perform dilation and erosion to remove some noise 
kernel = np.ones((1, 1), np.uint8) 
img = cv2.dilate(bin_img, kernel, iterations=1) 
img = cv2.erode(img, kernel, iterations=1) 

# Use pytesseract to convert the image data to text 
text = pytesseract.image_to_string(img ,lang='eng',) 

# Print the text 
print(text)