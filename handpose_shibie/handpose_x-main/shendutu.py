import cv2
import numpy as np


def red_shen(path, output_path):
    mean_depth = 0

    # 读取深度图像
    depth_image = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    # 检查图像是否读取成功
    if depth_image is None:
        raise ValueError("图像读取失败，请检查路径。")

    # 转换到HSV颜色空间（如果是RGB图像）
    hsv_image = cv2.cvtColor(depth_image, cv2.COLOR_BGR2HSV)

    # 定义红色的HSV范围
    lower_red_1 = np.array([0, 140, 46])
    upper_red_1 = np.array([10, 255, 255])
    lower_red_2 = np.array([156, 140, 46])
    upper_red_2 = np.array([180, 255, 255])

    # 创建掩码
    mask1 = cv2.inRange(hsv_image, lower_red_1, upper_red_1)
    mask2 = cv2.inRange(hsv_image, lower_red_2, upper_red_2)
    red_mask = cv2.bitwise_or(mask1, mask2)

    # 提取红色像素的深度值
    red_pixels_depth = depth_image[red_mask > 0]

    # 检查是否找到红色像素
    if len(red_pixels_depth) == 0:
        print("没有检测到红色像素。")
    else:
        # 输出红色像素的深度值
        print("红色像素的深度值：", red_pixels_depth)

        # 计算平均深度
        mean_depth = np.mean(red_pixels_depth)
        print("红色像素的平均深度值：", mean_depth)

        # 在原图像上标记红色像素的深度值
        output_image = depth_image.copy()
        red_coords = np.column_stack(np.where(red_mask > 0))

        # 分组处理每 100 个坐标中的一个坐标
        for i in range(0, len(red_coords), 1500):
            y, x = red_coords[i]
            depth_value = depth_image[y, x]
            cv2.putText(output_image, str(depth_value), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        # 保存结果图像
        cv2.imwrite(output_path, output_image)
        print(f"标记后的图像已保存到：{output_path}")

    return mean_depth

def bule_shen(path, output_path):
    mean_depth = 0

    # 读取深度图像
    depth_image = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    # 检查图像是否读取成功
    if depth_image is None:
        raise ValueError("图像读取失败，请检查路径。")

    # 转换到HSV颜色空间（如果是RGB图像）
    hsv_image = cv2.cvtColor(depth_image, cv2.COLOR_BGR2HSV)

    # 定义红色的HSV范围
    lower_red_1 = np.array([100, 43, 46])
    upper_red_1 = np.array([124, 255, 255])
    # lower_red_2 = np.array([156, 70, 46])
    # upper_red_2 = np.array([180, 255, 255])

    # 创建掩码
    mask1 = cv2.inRange(hsv_image, lower_red_1, upper_red_1)
    # mask2 = cv2.inRange(hsv_image, lower_red_2, upper_red_2)
    red_mask = mask1

    # 提取红色像素的深度值
    red_pixels_depth = depth_image[red_mask > 0]

    # 检查是否找到红色像素
    if len(red_pixels_depth) == 0:
        print("没有检测到蓝色像素。")
    else:
        # 输出红色像素的深度值
        print("蓝色像素的深度值：", red_pixels_depth)

        # 计算平均深度
        mean_depth = np.mean(red_pixels_depth)
        print("蓝色像素的平均深度值：", mean_depth)

        # 在原图像上标记红色像素的深度值
        output_image = depth_image.copy()
        red_coords = np.column_stack(np.where(red_mask > 0))

        # 分组处理每 100 个坐标中的一个坐标
        for i in range(0, len(red_coords), 1200):
            y, x = red_coords[i]
            depth_value = depth_image[y, x]
            cv2.putText(output_image, str(depth_value), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)

        # 保存结果图像
        cv2.imwrite(output_path, output_image)
        print(f"标记后的图像已保存到：{output_path}")

    return mean_depth

# 调用函数
image_path = 'D:/python_project/handpose_shibie/handpose_x-main/beifen/bs_sd.jpg'
output_path = 'D:/python_project/handpose_shibie/handpose_x-main/beifen/bs_marked_red.jpg'
output_path_b = 'D:/python_project/handpose_shibie/handpose_x-main/beifen/bs_marked_blue.jpg'
red_shen(image_path, output_path)
bule_shen(image_path,output_path_b)

