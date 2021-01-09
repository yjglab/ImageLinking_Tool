from tkinter import *

root = Tk()
root.title("GUI PROGRAM")
root.geometry("640x480+900+600") # 가로x세로+X+Y
root.resizable(False, False) # X(너비), Y(높이) 값 변경 불가

txt = Text(root, width=30 ,height=5) # 텍스트 위젯
txt.pack()

txt.insert(END, "글자를 입력하세요") # 위젯 순서. 

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력하세요") # 위젯 순서.

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1(line 1번째).0(column기준 0번째) 부터 END까지 불러옴
    print(e.get()) # Entry 값 불러옴

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()