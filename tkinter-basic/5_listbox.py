from tkinter import *

root = Tk()
root.title("GUI PROGRAM")
root.geometry("640x480+900+600") # 가로x세로+X+Y
root.resizable(False, False) # X(너비), Y(높이) 값 변경 불가

# list box : 여러 줄에 걸쳐 어떤 목록들을 관리하는 위젯

listbox = Listbox(root, selectmode="extended", height=0) 
# extended : 다중 선택, single : 한개 선택, height: 처음에 보일 목록 수 (0은 모두 보임)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "메론")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    listbox.delete(END) # 맨 뒤 리스트 항목 삭제 # 0: 맨 처음 항목 삭제, END: 마지막 항목 삭제
    # 개수 확인
    print("리스트에는", listbox.size(), "개가 있어요")
    # 항목 확인 (시작 idx, 끝 idx)
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))
    # 선택된 항목 확인 (위치로 반환)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()