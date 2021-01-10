from tkinter import *

root = Tk()
root.title("GUI PROGRAM")
root.geometry("640x480+900+600") 
root.resizable(False, False) 

# scrollbar => 스크롤 바와 스크롤 바 대상이 되는 위젯을 하나의 frame에 넣는것이 관리가 편함

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + "일") # 1일, 2일, ... 

listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # 맵핑

root.mainloop()