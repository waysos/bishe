import torch
import torchvision.transforms as transforms
import cv2
import numpy as np
from PIL import Image


# 加载预训练的 MiDaS 模型
model_type = "DPT_Large"  # 或者 "MiDaS_small", "MiDaS_v2.1", "DPT_Hybrid", "DPT_Large"
midas = torch.hub.load("intel-isl/MiDaS", model_type)

# 将模型设置为评估模式
midas.eval()

# 创建预处理转换
midas_transforms = transforms.Compose([
    transforms.ToPILImage(),  # 将图像转换为 PIL 图像对象
    transforms.Resize(384),   # 调整图像大小为模型的输入尺寸
    transforms.ToTensor(),    # 将图像转换为张量
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # 标准化图像
])


def image_to_depth(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 转换图像到 PyTorch 张量并进行预处理
    input_tensor = midas_transforms(image).unsqueeze(0)

    # 推理并获取深度图
    with torch.no_grad():
        prediction = midas(input_tensor)

    # 将深度图转换为 NumPy 数组
    depth_map = prediction.squeeze().cpu().numpy()

    return depth_map


# # 示例使用
# image_path = "D:/python_project/handpose_shibie/handpose_x-main/beifen/bs.jpg"  # 替换为你的图像路径
# depth_map = image_to_depth(image_path)
# # print(depth_map)
#
# # 保存深度图
# cv2.imwrite("D:/python_project/handpose_shibie/handpose_x-main/beifen/bs_sd.jpg", (depth_map * 255).astype(np.uint8))
