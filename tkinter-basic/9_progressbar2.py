import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI PROGRAM")
root.geometry("640x480+900+600") # 가로x세로+X+Y
root.resizable(False, False) # X(너비), Y(높이) 값 변경 불가

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 보여주기 용 # 0.01초 대기

        p_var2.set(i) # progress bar 값 설정
        progressbar2.update() # ui 업데이트
        

btn = Button(root, text="시작하기", command=btncmd2)
btn.pack()

root.mainloop()
