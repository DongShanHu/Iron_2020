import win32api
import win32con
import time
import random


def move_click(x, y, t=0):  # 移動滑鼠並點選左鍵
    win32api.SetCursorPos((x, y))  # 設定滑鼠位置(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                         win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 點選滑鼠左鍵
    if t == 0:
        time.sleep(random.random()*2+1)  # sleep一下
    else:
        time.sleep(t)
    return 0


move_click(210, 96)
