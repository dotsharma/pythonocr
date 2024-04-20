import easyocr

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Read text from image
result = reader.readtext('test4.png')

# Process the result
for detection in result:
    text = detection[1]
    print(text)
