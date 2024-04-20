import cv2

# Load the image
image = cv2.imread(r"C:\Users\Admin\Downloads\WhatsAppImages.png")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur for noise reduction
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Enhance contrast using adaptive histogram equalization
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced = clahe.apply(blurred)

# Apply adaptive thresholding
thresh = cv2.adaptiveThreshold(enhanced, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)

# Perform dilation and erosion for text enhancement
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated = cv2.dilate(thresh, kernel, iterations=1)
eroded = cv2.erode(dilated, kernel, iterations=1)

# Invert the image
inverted = cv2.bitwise_not(eroded)

# Save the preprocessed image
cv2.imwrite('preprocessed_image.jpg', inverted)
