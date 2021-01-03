import  cv2
import  pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Log Head\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread(r'C:\Users\Log Head\Documents\Programming\spellingQuiz\data\typingtest38\Capture.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
cv2.imshow('testing', img)
cv2.waitKey(0)