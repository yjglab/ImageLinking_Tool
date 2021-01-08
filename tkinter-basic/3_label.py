from tkinter import *

root = Tk()
root.title("GUI PROGRAM")
root.geometry("640x480+900+600") # 가로x세로+X+Y
root.resizable(False, False) # X(너비), Y(높이) 값 변경 불가

label1 = Label(root, text="hello")
label1.pack()

photo = PhotoImage(file="tkinter-basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="see you later") # 변경

    global photo2 # 지역변수로 설정해두면 garbage collector로 인해 삭제됨.
    photo2 = PhotoImage(file="tkinter-basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()