from tkinter import *

root = Tk()
root.title("GUI PROGRAM")
root.geometry("640x480+900+600") 
root.resizable(False, False) 

btn1 = Button(root, text="버튼1")
btn2 = Button(root, text="버튼2")

# pack()은 쌓는 느낌, grid는 지정된 곳에 두는 형태
# btn1.pack(side="left")
# btn2.pack()

btn1.grid(row=0, column=0) # (0, 0)
btn2.grid(row=1, column=1) # (1, 1)

root.mainloop()