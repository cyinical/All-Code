import pyautogui, time,os

w = pyautogui.typewrite
e = pyautogui.press

x = 1000
while x != 0:
    w('save-all')
    e("enter")
    x = x - 1
    print(x)
    time.sleep(100)

#if x == 0:
#    w('stop')
#    e("enter")
#    os._exit(1)
