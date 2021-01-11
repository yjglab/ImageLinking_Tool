import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI PROGRAM")
root.geometry("640x480+900+600") # 가로x세로+X+Y
root.resizable(False, False) # X(너비), Y(높이) 값 변경 불가

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정 + 값 입력도 가능

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 별도의 값 입력 불가
readonly_combobox.current(5) # 5번 index 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get()) # 선택된 값
    print(readonly_combobox.get())

btn = Button(root, text="선택하기", command=btncmd)
btn.pack()

root.mainloop()