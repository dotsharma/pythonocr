# import cv2
# import pytesseract

# # Path to Tesseract executable (change this according to your system)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Load the preprocessed image
# preprocessed_image = cv2.imread('preprocessed_image.jpg')

# # Convert the preprocessed image to grayscale
# gray_image = cv2.cvtColor(preprocessed_image, cv2.COLOR_BGR2GRAY)

# # Use Pytesseract to extract text
# extracted_text = pytesseract.image_to_string(gray_image)

# # Print the extracted text
# print(extracted_text)


# import cv2
# import pytesseract

# # Path to Tesseract executable (change this according to your system)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Load the problematic image
# image = cv2.imread(r"C:\Users\Admin\Downloads\WhatsAppImages.png")

# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply contrast enhancement
# enhanced_image = cv2.equalizeHist(gray_image)

# # Use a noise reduction technique (Gaussian blur)
# blurred_image = cv2.GaussianBlur(enhanced_image, (5, 5), 0)

# # Apply adaptive thresholding
# _, thresholded_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# # Invert the colors of the image
# inverted_image = cv2.bitwise_not(thresholded_image)

# # Use Pytesseract to extract text
# extracted_text = pytesseract.image_to_string(inverted_image)

# # Print the extracted text
# print(extracted_text)


import cv2
import pytesseract

# Path to Tesseract executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the problematic image
image = cv2.imread(r"C:\Users\Admin\Downloads\WhatsAppImages.png")


# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur for noise reduction
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply adaptive thresholding
# _, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# Invert the colors of the image
inverted_image = cv2.bitwise_not(blurred_image)

# cv2.imwrite('test4.png', inverted_image)
# Use Pytesseract to extract text
extracted_text = pytesseract.image_to_string(inverted_image)

# Print the extracted text
print(extracted_text)

#  image = cv2.imread(r"C:\Users\Admin\Downloads\WhatsAppImages.png")

# import cv2
# import pytesseract

# # Path to Tesseract executable (change this according to your system)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Load the image
# image = cv2.imread(r"C:\Users\Admin\Downloads\WhatsAppImages.png")

# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply adaptive thresholding to enhance the text
# thresh_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# # Use Pytesseract to extract text
# extracted_text = pytesseract.image_to_string(thresh_image, lang='eng')

# # Print the extracted text
# print(extracted_text)


