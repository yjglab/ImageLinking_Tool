# keyboard 모듈 : 사용자가 특정한 키를 입력했을 때 해당 값을 맞추어 동작하는 모듈 (pip install keyboard)
import time
import keyboard
from PIL import ImageGrab

def screenshot():
    cur_time = time.strftime("_%Y%m%d_%H%M%S") # "_20210114_032420"
    img = ImageGrab.grab()
    img.save("img{}.png".format(cur_time)) # img_20210114_032420.png

keyboard.add_hotkey("F9", screenshot) # ctrl+shift+s 등의 조합도 가능
keyboard.wait("esc") # esc를 누를 때까지 동작