import tkinter as tk
import random
import threading
import time
import sys

def show_warn_tip():
    """创建并显示随机位置的提示窗口"""
    # 创建窗口
    window = tk.Tk()
    
    # 获取屏幕尺寸（确保在窗口创建后获取）
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # 窗口尺寸
    window_width = 250
    window_height = 60
    
    # 随机位置（确保窗口在屏幕内）
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)
    
    # 设置窗口位置和标题
    window.title("小雨宝宝")
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # 提示语列表（已添加新内容）
    tips = [
  "多喝水啊",
  "保持微笑",
  "每天快乐呀",
  "记得吃水果",
  "保持好心情",
  "好好爱自己",
  "我想你了",
  "多想我呀",
  "想住进你心里",
  "一辈子都守护你",
  "相信美好会关注到你哦",
  "天冷了，多穿衣服",
  "按时吃饭，你的胃我来操心",
  "早点休息，别熬夜",
  "累了就歇歇，我在这儿呢",
  "出门记得带伞，别淋雨了",
  "工作再忙，也要记得站起来活动一下",
  "你笑起来的样子，真的很好看",
  "你是我心尖上的宝贝",
  "遇见你，是我最幸运的事",
  "我的心里，早已被你填满",
  "无论在哪，我都想奔向你",
  "和你在一起的每一天，都闪着光",
  "你就是我的美好本身",
  "有你在，未来可期",
  "你值得世间所有美好",
  "没关系，你已经做得很好了",
  "在我这里，你永远是最特别的存在",
  "别怕，有我陪着你呢",
  "慢慢来，我会等你",
  "你本身就是一道风景",
  "今天的你，也辛苦啦"
]
    
    tip = random.choice(tips)
    
    # 随机背景颜色（淡色系）
    bg_colors = [
        'lightpink', 'skyblue',
        'lightgreen', 'lavender',
        'lightyellow', 'plum', 'coral',
        'bisque', 'aquamarine',
        'mistyrose', 'honeydew',
        'lavenderblush', 'oldlace'
    ]
    
    bg = random.choice(bg_colors)
    
    # 创建标签显示文字
    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=('微软雅黑', 16),
        width=20,
        height=3
    ).pack()
    
    # 窗口置顶显示
    window.attributes('-topmost', True)
    
    # 绑定关闭事件，触发时退出所有窗口
    def on_space(event):
        window.destroy()
        # 遍历所有线程，关闭所有tkinter窗口
        for t in threads:
            if t.is_alive():
                # tkinter窗口关闭后线程自然结束
                pass
        sys.exit()  # 退出程序
    
    window.bind('<space>', on_space)
    
    # 主循环显示窗口
    window.mainloop()


# 创建线程列表
threads = []

# 窗口数量（根据屏幕尺寸大小可调整）
for i in range(77):
    t = threading.Thread(target=show_warn_tip)
    threads.append(t)
    t.start()
    time.sleep(0.05)  # 快速连续出现窗口


