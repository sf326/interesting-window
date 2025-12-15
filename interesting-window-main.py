#by sf
#按下小键盘的'1'键可以快速退出程序


from tkinter import Tk
import tkinter as tk
import random
import threading
import time
import base64
import os
import keyboard


#可留空 弹窗的ico图标(base64解码)
sfico = ""

#必填 窗口名称
sfname = "sf"

#必填 窗口文字字体
sffonts = "黑体"

#必填 窗口文字大小
sffontssize = "12"

#必填 等待多少秒后开始创建窗口
sftime = "0.5"


#可留空 背景颜色列表 没有的话有自带的列表自动随机
color_list = [


]


#必填 随机文字
text_list = [
    "天天开心ฅ",
    "很高兴遇见你 不可思议的14亿分之一 =^_^=",
    "海内存知己 天涯若比邻",
    "许个愿 许你自由愿你无忧˶˃ ᵕ ˂˶ಣ",
]




def create_random_window():
    new_window = tk.Toplevel()
    
    new_window.withdraw()

    color_names = [
        "red", "green", "blue", "yellow", "purple", "orange", "pink", 
        "gray", "white", "cyan", "magenta", "lime",
        "teal", "navy", "gold", "silver", "indigo", "violet", "coral",
        "salmon", "khaki", "ivory", "lavender", "maroon", "olive", "plum"
    ]

    if color_list and len(color_list) > 0:
        bg_color = random.choice(color_list)
    else:
        bg_color = random.choice(color_names)
    
    if text_list and len(text_list) > 0:
        display_text = random.choice(text_list)
    else:
        display_text = "error"
    
    new_window.configure(bg=bg_color)
    new_window.attributes('-topmost', True)
    
    if sfico:
        try:
            tmp_icon = open("temp_icon.ico", "wb+")
            tmp_icon.write(base64.b64decode(sfico))
            tmp_icon.close()
            new_window.iconbitmap("temp_icon.ico")
            os.remove("temp_icon.ico")
        except Exception as e:
            print(f"图标设置失败: {e}")
    
    label = tk.Label(new_window, 
                     text=display_text, 
                     font=(sffonts, sffontssize),
                     bg=bg_color)
    label.pack(pady=20)

    new_window.update()
    new_window.update_idletasks()
    
    window_width = new_window.winfo_width()
    window_height = new_window.winfo_height()
    
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    
    x = random.randint(0, max(1, screen_width - window_width))
    y = random.randint(0, max(1, screen_height - window_height))
    
    new_window.geometry(f"+{x}+{y}")

    new_window.deiconify()
    new_window.lift()
    new_window.focus_force()

def window_generator():
    root = Tk()
    root.title(sfname)
    root.withdraw()

    print("初始化成功! The py by sf.")

    global running
    
    while running:
        create_random_window()
        time.sleep(0.02)

def check_exit_key():
    global running
    while running:
        if keyboard.is_pressed('num 1') or keyboard.is_pressed('1'):
            print("检测到退出按键，正在关闭所有窗口...")
            running = False
            break
        time.sleep(0.05)


def main():
    print("by sf.")
    print(f"将在 {sftime} 秒后开始")
    time.sleep(float(sftime))

    global running, windows

    running = True
    windows = []
    
    try:
        generator_thread = threading.Thread(target=window_generator, daemon=True)
        generator_thread.start()
        
        key_thread = threading.Thread(target=check_exit_key, daemon=True)
        key_thread.start()
        
        print("程序已启动，每隔0.02秒生成一个随机窗口")
        print("按下小键盘的'1'键退出程序")
        
        while running:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        running = False
    finally:
        print("程序已退出")

if __name__ == "__main__":
    main()
