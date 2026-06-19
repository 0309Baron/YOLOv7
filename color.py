import cv2
import numpy as np

# 读取图像
image = cv2.imread(r'runs\detect\exp\1.jpg')
# 将图像转换为 HSV 格式
print(image.shape)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义蓝色的 HSV 范围
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# 使用 inRange 函数提取蓝色区域
mask = cv2.inRange(hsv, lower_red, upper_red)

# 查找轮廓
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 获取轮廓的坐标
f=[]
g=[]
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    f.append(x)
    g.append(y)
x=(max(f)+min(f))/2
y=(max(g)+min(g))/2
print(x,y)
b=int(image.shape[0]/3)
c=int(image.shape[1]/3)
for i in range(3):
    if x<=c*(i+1) and x>=c*i:
        d=i
for i in range(3):
    if y<=b*(i+1) and y>=b*i:
        e=i
out=(d+1)+e*3
print(out)
