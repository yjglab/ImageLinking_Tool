import time
from PIL import ImageGrab # python image ilbrary

time.sleep(5) # 5초 대기 준비시간

for i in range(1, 11): # 2초 간격 10장 저장
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save("image{}.png".format(i)) # 파일로 저장 
    time.sleep(1)