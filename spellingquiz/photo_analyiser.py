#TODO find location of keyboard. I have location given by user within the JSON file which might help

#TODO (WIP)find location of each finger

import cv2

testimage = r"C:\Users\Log Head\Documents\Programming\spellingquiz-git\spellingquiz\data\typingtest0\1608069460713.png"


img = cv2.imread(testimage)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('grey', gray)



kernel_size = 5 #kernel size must be odd number
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)
cv2.imshow(f'GaussuanBlur kernel_size = {kernel_size}', blur_gray)


low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
cv2.imshow('canny', edges)

cv2.waitKey(0)
