import cv2
import numpy as np

# 이미지 읽기
img = cv2.imread('image.jpg')

while img is not None:
    # 이미지 전처리
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5,7)
    color = cv2.bilateralFilter(img, 3, 500, 500)

    # 두 이미지 합성
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # 원본 이미지와 붙이기
    cartoon = np.hstack((img,cartoon))

    # 출력
    cv2.imshow("Original | Cartoon Rendering", cartoon)
    key = cv2.waitKey(0)
    if key == 27:
        break
cv2.destroyAllWindows()

