import cv2
import numpy as np

# 读取图像
image = cv2.imread(r'runs\detect\exp\1.jpg')

# 将图像转换为 HSV 格式
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义蓝色的 HSV 范围
lower_blue = np.array([0, 100, 100])
upper_blue = np.array([10, 255, 255])

# 使用 inRange 函数提取蓝色区域
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# 查找轮廓
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 获取轮廓的坐标
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    print(f'坐标：({x}, {y}), 宽度：{w}, 高度：{h}')

# 在图像上绘制识别出的蓝色区域
result = cv2.bitwise_and(image, image, mask=mask)

# 显示图像
cv2.imshow('Original Image', image)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
