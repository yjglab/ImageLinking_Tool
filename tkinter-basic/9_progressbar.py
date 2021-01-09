import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI PROGRAM")
root.geometry("640x480+900+600") # 가로x세로+X+Y
root.resizable(False, False) # X(너비), Y(높이) 값 변경 불가

progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # mode 중 indeterminate도 있음.
progressbar.start(10) # 지정 ms마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop()

btn = Button(root, text="중지하기", command=btncmd)
btn.pack()

root.mainloop()