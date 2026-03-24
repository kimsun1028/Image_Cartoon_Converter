import cv2 as cv
import numpy as np

# 이미지 읽기
img = cv.imread('image.jpg')

while img is not None:
    # 이미지 전처리
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 3)
    edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5,7)
    color = cv.bilateralFilter(img, 3, 500, 500)

    # 두 이미지 합성
    cartoon = cv.bitwise_and(color, color, mask=edges)

    # 출력
    cv.imshow("Cartoon Rendering", cartoon)
    key = cv.waitKey(0)
    if key == 27:
        break
cv.destroyAllWindows()

