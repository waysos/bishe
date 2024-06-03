from datetime import datetime
import json
import os


def is_empty_file(file_path):
    return os.path.getsize(file_path) == 0
def xieru(score_SIE, score_touch, zong_score, score_FMA, score_MSS):
    # 指定 JSON 文件路径
    file_path = "data.json"
    socre_dicts = []
    score_dict = {
        "score_SIE": None,
        "score_touch": None,
        "zong_score": None,
        "score_FMA": None,
        "score_MSS": None,
        "time": None
    }
    # 检查文件是否存在
    if not os.path.exists(file_path):
        # 如果文件不存在，则创建一个新文件
        with open(file_path, "w") as json_file:
            json.dump({}, json_file)

        print("已创建新的 JSON 文件。")
    if is_empty_file(file_path):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        score_dict["score_SIE"] = score_SIE
        score_dict["score_touch"] = score_touch
        score_dict["zong_score"] = zong_score
        score_dict["score_FMA"] = score_FMA
        score_dict["score_MSS"] = score_MSS
        score_dict["time"] = current_time

        # 更新现有数据
        socre_dicts.append(score_dict)

        # 将更新后的数据写入 JSON 文件中
        with open(file_path, "w") as json_file:
            json.dump(socre_dicts, json_file, indent=4)
    else:
        # 加载现有的 JSON 数据
        with open(file_path, "r") as json_file:
            existing_data = json.load(json_file)

        for i in range(len(existing_data)):
            socre_dicts.append(existing_data[i])

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        score_dict["score_SIE"] = score_SIE
        score_dict["score_touch"] = score_touch
        score_dict["zong_score"] = zong_score
        score_dict["score_FMA"] = score_FMA
        score_dict["score_MSS"] = score_MSS
        score_dict["time"] = current_time

        # 更新现有数据
        socre_dicts.append(score_dict)

        # 将更新后的数据写入 JSON 文件中
        with open(file_path, "w") as json_file:
            json.dump(socre_dicts, json_file, indent=4)


def jisuan(score_SIE, score_touch, score_FMA, score_MSS):
    zong_score = score_SIE * 0.4 + score_touch * 0.3 + (score_FMA + score_MSS) * 0.5

    return score_SIE, score_touch, zong_score, score_FMA, score_MSS

def tet():
    score_SIE, score_touch, zong_score, score_FMA, score_MSS = jisuan(75.1824, 87.59281, 11, 30)
    xieru(score_SIE, score_touch, zong_score, score_FMA, score_MSS)









