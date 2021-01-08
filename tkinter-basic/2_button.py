from tkinter import *

root = Tk()
root.title("GUI PROGRAM")
root.geometry("640x480+900+600") # 가로x세로+X+Y
root.resizable(False, False) # X(너비), Y(높이) 값 변경 불가

btn1 = Button(root, text="button1")
btn1.pack() # 호출

btn2 = Button(root, padx=5, pady=10, text="button2") # padding 값
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="button3") 
btn3.pack()

btn4 = Button(root, width=10, height=3, text="button4") 
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="button5")
btn5.pack()

photo = PhotoImage(file="tkinter-basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("button clicked")
btn7 = Button(root, text="working button", command=btncmd)
btn7.pack()

root.mainloop()