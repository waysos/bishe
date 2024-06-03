from tkinter import *
import tkinter.filedialog
import tui_li_z
import os
import threading
import json

selected_file_muzhi_1 = None
selected_file_shizhi_1 = None
selected_file_zhongzhi_1 = None
selected_file_huanzhi_1 = None
selected_file_xiaozhi_1 = None
selected_file_sizhi = None
selected_file_muzhi = None

def is_empty_file(file_path):
    return os.path.getsize(file_path) == 0

def xz(lb):
    global selected_file_muzhi_1
    filename=tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text='您已选择文件-拇指按触', fg='green')
         selected_file_muzhi_1 = filename
    else:
         lb.config(text='您没有选择任何文件', fg='red')

def xz1(lb):
    global selected_file_shizhi_1
    filename=tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text='您已选择文件-食指按触', fg='green')
         selected_file_shizhi_1 = filename
    else:
         lb.config(text='您没有选择任何文件', fg='red')

def xz2(lb):
    global selected_file_zhongzhi_1
    filename=tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text='您已选择文件-中指按触', fg='green')
         selected_file_zhongzhi_1 = filename
    else:
         lb.config(text='您没有选择任何文件', fg='red')

def xz3(lb):
    global selected_file_huanzhi_1
    filename=tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text='您已选择文件-环指按触', fg='green')
         selected_file_huanzhi_1 = filename
    else:
         lb.config(text='您没有选择任何文件', fg='red')

def xz4(lb):
    global selected_file_xiaozhi_1
    filename=tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text='您已选择文件-小指按触', fg='green')
         selected_file_xiaozhi_1 = filename
    else:
         lb.config(text='您没有选择任何文件', fg='red')

def xz5(lb):
    global selected_file_sizhi
    filename=tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text='您已选择文件-四指角度', fg='green')
         selected_file_sizhi = filename
    else:
         lb.config(text='您没有选择任何文件', fg='red')

def xz6(lb):
    global selected_file_muzhi
    filename=tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text='您已选择文件-姆指角度', fg='green')
         selected_file_muzhi = filename
    else:
         lb.config(text='您没有选择任何文件', fg='red')

def yunxing(lb):
    global zong_socre, socre_touch, socre_SIE
    lb.config(text='运行中', fg='blue')
    zong_socre, socre_touch, socre_SIE = tui_li_z.zhongyao(selected_file_muzhi_1, selected_file_shizhi_1, selected_file_zhongzhi_1, selected_file_huanzhi_1,
                      selected_file_xiaozhi_1, selected_file_sizhi, selected_file_muzhi, socre_FMA, socre_MSS)
    lb.config(text='运行结束', fg='green')

def start_task_thread(lb, a, b):
    global socre_FMA, socre_MSS
    socre_FMA = float(a)
    socre_MSS = float(b)
    task_thread = threading.Thread(target=yunxing, args=(lb,))
    task_thread.start()


def huoquchengji(lb, num):
    if num == 0:
        chengji = "总成绩为：%s" % zong_socre
        lb.config(text=chengji, fg='green')
    elif num == 1:
        chengji = "按触成绩为：%s" % socre_touch
        lb.config(text=chengji, fg='green')
    elif num == 2:
        chengji = "SIE成绩为：%s" % socre_SIE
        lb.config(text=chengji, fg='green')

def open_folder(folder_path):
    os.system(f'explorer {folder_path}')  # Windows 系统下的打开文件夹命令

def wenjianjia(lb):
    # 获取当前.py文件所在的目录路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    picture_dir = os.path.join(current_dir, 'picture')
    open_folder(picture_dir)
    lb.config(text="已经打开相关文件夹", fg='green')

def createNewWindow():
    app = Tk()
    app.geometry('960x480')
    app.title('记录查询')

    idx = 0

    file_path = "data.json"
    # 检查文件是否存在
    if not os.path.exists(file_path):
        # 如果文件不存在，则创建一个新文件
        with open(file_path, "w") as json_file:
            json.dump({}, json_file)

        print("已创建新的 JSON 文件。")

    if is_empty_file(file_path):
        lb1 = Label(app, text='无相关记录', font=("黑体", 10), fg='blue')
        lb1.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.1)
    else:
        with open(file_path, "r") as json_file:
            existing_data = json.load(json_file)

        for i in range(len(existing_data)):
            idx += 1
            score_SIE = existing_data[i]["score_SIE"]
            score_touch = existing_data[i]["score_touch"]
            zong_score = existing_data[i]["zong_score"]
            score_FMA = existing_data[i]["score_FMA"]
            score_MSS = existing_data[i]["score_MSS"]
            time = existing_data[i]["time"]

            txt_name = str(idx)

            txt_time = time
            txt_SIE = " SIE测试成绩:" + str(score_SIE)
            txt_touch = " 按触测试成绩:" + str(score_touch)
            txt_zong = " 总测试成绩:" + str(zong_score)
            txt_FMA = " FMA测试成绩:" + str(score_FMA)
            txt_MSS = " MSS测试成绩:" + str(score_MSS)

            txt = txt_name + " " + txt_time + txt_zong + txt_SIE + txt_touch + txt_FMA + txt_MSS

            lb = Label(app, text=txt, font=("黑体", 9))
            # lb.place(relx=0.001, rely=0.06*idx, relwidth=1, relheight=0.06, anchor='w')
            lb.place(x = 50, y = 30*idx, anchor = 'w')

            if idx > 15:
                break







def jiemian():
    filenames = []
    root = Tk()
    root.geometry('960x480')
    root.title('手部按触功能障碍辅助评估系统')

    lb1 = Label(root, text='手部按触功能障碍辅助评估系统', font=("黑体", 20))
    lb1.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.1)

    lb2 = Label(root, text='请输入患者拇指按触视频', font=("黑体", 10))
    lb2.place(relx=0.01, rely=0.1, relwidth=0.2, relheight=0.1)
    btn2 = Button(root, text='选择文件', command=lambda: xz(lb2))
    btn2.place(relx=0.21, rely=0.12, relwidth=0.15, relheight=0.06)


    lb3 = Label(root, text='请输入患者食指按触视频', font=("黑体", 10))
    lb3.place(relx=0.01, rely=0.2, relwidth=0.2, relheight=0.1)
    btn3 = Button(root, text='选择文件', command=lambda: xz1(lb3))
    btn3.place(relx=0.21, rely=0.22, relwidth=0.15, relheight=0.06)

    lb4 = Label(root, text='请输入患者中指按触视频', font=("黑体", 10))
    lb4.place(relx=0.01, rely=0.3, relwidth=0.2, relheight=0.1)
    btn4 = Button(root, text='选择文件', command=lambda: xz2(lb4))
    btn4.place(relx=0.21, rely=0.32, relwidth=0.15, relheight=0.06)

    lb5 = Label(root, text='请输入患者环指按触视频', font=("黑体", 10))
    lb5.place(relx=0.01, rely=0.4, relwidth=0.2, relheight=0.1)
    btn5 = Button(root, text='选择文件', command=lambda: xz3(lb5))
    btn5.place(relx=0.21, rely=0.42, relwidth=0.15, relheight=0.06)

    lb6 = Label(root, text='请输入患者小指按触视频', font=("黑体", 10))
    lb6.place(relx=0.01, rely=0.5, relwidth=0.2, relheight=0.1)
    btn6 = Button(root, text='选择文件', command=lambda: xz4(lb6))
    btn6.place(relx=0.21, rely=0.52, relwidth=0.15, relheight=0.06)

    lb7 = Label(root, text='请输入患者四指角度视频', font=("黑体", 10))
    lb7.place(relx=0.01, rely=0.6, relwidth=0.2, relheight=0.1)
    btn7 = Button(root, text='选择文件', command=lambda: xz5(lb7))
    btn7.place(relx=0.21, rely=0.62, relwidth=0.15, relheight=0.06)

    lb8 = Label(root, text='请输入患者拇指角度视频', font=("黑体", 10))
    lb8.place(relx=0.01, rely=0.7, relwidth=0.2, relheight=0.1)
    btn8 = Button(root, text='选择文件', command=lambda: xz6(lb8))
    btn8.place(relx=0.21, rely=0.72, relwidth=0.15, relheight=0.06)

    lb9 = Label(root, text='点击下面按钮运行程序，一般需要大约6分钟', font=("黑体", 10))
    lb9.place(relx=0.35, rely=0.82, relwidth=0.3, relheight=0.08)
    btn9 = Button(root, text='运行', command=lambda: start_task_thread(lb9, inp1.get(), inp2.get()))
    btn9.place(relx=0.43, rely=0.9, relwidth=0.14, relheight=0.06)

    lb14 = Label(root, text='请输入FMA评估分数')
    lb14.place(relx=0.46, rely=0.1, relwidth=0.3, relheight=0.1)
    inp1 = Entry(root)
    inp1.place(relx=0.76, rely=0.12, relwidth=0.15, relheight=0.06)

    lb15 = Label(root, text='请输入MSS评估分数')
    lb15.place(relx=0.46, rely=0.2, relwidth=0.3, relheight=0.1)
    inp2 = Entry(root)
    inp2.place(relx=0.76, rely=0.22, relwidth=0.15, relheight=0.06)

    lb10 = Label(root, text='运行结束后，点击右侧按钮获取总评估成绩', font=("黑体", 10))
    lb10.place(relx=0.46, rely=0.3, relwidth=0.3, relheight=0.1)
    btn10 = Button(root, text='获取成绩', command=lambda: huoquchengji(lb10, 0))
    btn10.place(relx=0.76, rely=0.32, relwidth=0.15, relheight=0.06)

    lb11 = Label(root, text='运行结束后，点击右侧按钮获取按触成绩', font=("黑体", 10))
    lb11.place(relx=0.452, rely=0.4, relwidth=0.3, relheight=0.1)
    btn11 = Button(root, text='获取成绩', command=lambda: huoquchengji(lb11, 1))
    btn11.place(relx=0.76, rely=0.42, relwidth=0.15, relheight=0.06)

    lb12 = Label(root, text='运行结束后，点击右侧按钮获取SIE成绩', font=("黑体", 10))
    lb12.place(relx=0.45, rely=0.5, relwidth=0.3, relheight=0.1)
    btn12 = Button(root, text='获取成绩', command=lambda: huoquchengji(lb12, 2))
    btn12.place(relx=0.76, rely=0.52, relwidth=0.15, relheight=0.06)

    lb13 = Label(root, text='运行结束后，点击下面按钮打开手部运动变化相关文件夹', font=("黑体", 10))
    lb13.place(relx=0.45, rely=0.6, relwidth=0.5, relheight=0.1)
    btn13 = Button(root, text='打开文件夹', command=lambda: wenjianjia(lb13))
    btn13.place(relx=0.63, rely=0.7, relwidth=0.14, relheight=0.06)


    buttonExample = Button(root, text="查询记录", command=lambda: createNewWindow())
    buttonExample.place(relx=0.80, rely=0.9, relwidth=0.1, relheight=0.06)


    root.mainloop()

def jiemian_z():
    jiemian()

if __name__ == '__main__':
    jiemian_z()


