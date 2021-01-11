# from tkinter import *

# root = Tk()

# title = "제목없음"
# root.title("{0} - Windows 메모장".format(title))
# root.geometry("640x480+900+600") 

# frame = Frame(root)
# frame.pack()

# main_textbox = Text(frame)
# main_textbox.pack(fill="both", expand=True)

# def open_file(text):
#     with open("mynote.txt", "w", encoding="utf8") as mynote_file:
#         mynote_file.write(text)

# menu = Menu(root)
# menu_file = Menu(menu, tearoff=0)
# menu_file.add_command(label="Open")
# menu_file.add_command(label="Save", command=open_file)
# menu_file.add_command(label="Exit")
# menu.add_cascade(label="파일(F)", menu=menu_file)

# scrollbar = Scrollbar(frame)
# scrollbar.pack(side="right", fill="y")

# root.config(menu=menu)
# root.mainloop()

import os
from tkinter import *

root = Tk()
root.title("제목없음")
root.geometry("640x480+900+600") # 가로x세로+X+Y

filename = "mynote.txt"

def handle_open():
    if os.path.isfile(filename): 
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 삭제 후
            txt.insert(END, file.read()) # 본문에 내용 로드

def handle_save():
    with open(filename, "w", encoding="utf8") as file:
            file.write(txt.get("1.0", END))


menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="open...", command=handle_open)
menu_file.add_command(label="save", command=handle_save)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집") 
menu.add_cascade(label="서식") 
menu.add_cascade(label="보기") 
menu.add_cascade(label="도움말") 

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)
root.config(menu=menu)

root.mainloop()