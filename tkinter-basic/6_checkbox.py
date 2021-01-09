from tkinter import *

root = Tk()
root.title("GUI PROGRAM")
root.geometry("640x480+900+600") # 가로x세로+X+Y
root.resizable(False, False) # X(너비), Y(높이) 값 변경 불가

chkvar = IntVar() # chkvar에 int형으로 값을 저장
chkbox = Checkbutton(root, text="WUGO테스트 하기", variable=chkvar)
# chkbox.select() # 자동 선택처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="웹서버 제어하기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: 체크 해제, 1: 체크 됨
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()