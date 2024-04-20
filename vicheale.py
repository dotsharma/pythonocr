import cv2
import easyocr
from PIL import Image

# Load the image
image_path = r'collage.png'
image = cv2.imread(image_path)

# Resize the image for better processing speed (optional)
# resized_image = cv2.resize(image, (800, 600), interpolation=cv2.INTER_AREA)  # Example dimensions

# Convert the resized image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply adaptive thresholding to binarize the image
threshold_image = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Perform text extraction
result = reader.readtext(threshold_image)

# Print extracted text
for detection in result:
    print(detection[1])  # Print the detected text

# Display the preprocessed image
cv2.imshow('Preprocessed Image', threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

