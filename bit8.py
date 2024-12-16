import cv2
import numpy as np

img = np.zeros((1024, 2048), np.int8)  # 创建一个8bit的数据
img = cv2.imwrite("1.png", img)  # 存储后其图像依然为8bit的图像

img = cv2.imread("img.png", 0)  # 以单通道的格式打开
img = cv2.imwrite("2.png", img)  # 存储后依然是单通道
#
# img1 = cv2.imread("./frankfurt_000000_000294_gtFine_labelIds.png",0)
# img2 = cv2.imread("./2.png",0)
# # print(img1.shape[0])  # hight
# for i in range(img1.shape[0]):
#     for j in range(img1.shape[1]):
#         if img1[i][j] != img2[i][j]:
#             print("bug!")
#         else:
#             print("The point of "+str(i)+"_"+str(j)+" row:"+"is ok!")     # 比对两幅图的像素值一致
