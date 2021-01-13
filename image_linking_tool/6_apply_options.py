import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog # 서브 모듈. 별도 지정 필요
from PIL import Image
root = Tk()
root.title("이미지 연결 도구")
# root.geometry("640x480+900+600") 

# 파일 추가 
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일 선택", \
        filetypes=(("JPEG 파일 (*.jpg)", "*.jpg"), ("PNG 파일 (*.png)", "*.png"), ("BMP 파일 (*.bmp)", "*.png"),("모든 파일 (*.*)", "*.*")), \
            initialdir=r"C:\JaeGyeong\github-repository") # r: string 있는 그대로 읽음
            # 최초에 C:/ 경로를 표시함
    
    for file in files:
        list_file.insert(END, file)    

# 선택 삭제
def del_file():
    # reversed() : index 순서를 뒤집은 새로운 값. 원본에는 영향을 미치지 않음.
    for index in reversed(list_file.curselection()): 
        list_file.delete(index)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "": # 사용자가 취소 누르면
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합 
def merge_img():
    try:
        # 가로 넓이 
        img_width = cmb_width.get()
        if img_width == "원본 유지":
            img_width = -1
        else:
            img_width = int(img_width)

        # 간격 
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:
            img_space = 0

        # 포맷
        img_format = cmb_format.get().lower()

        images = [Image.open(i) for i in list_file.get(0, END)]
        # 현재 images 내 객체들은 size 값을 가지고 있음. # size[0] : width, size[1] : height
        # widths = [i.size[0] for i in images]  # heights = [i.size[1] for i in images] 
        
        # 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = [] # [(width1, height1), (width2, height2), ... ]
        if img_width > -1:
            # width는 cmb값, height는 변경될 width 값에 맞춰 비율을 조정함 => x:y=x':y' | xy'=x'y | y'=x'y/x 
            image_sizes = [(int(img_width), int(img_width * i.size[1] / i.size[0])) for i in images] 
        else: # 원본 사이즈 사용
            image_sizes = [(i.size[0], i.size[1]) for i in images]



        widths, heights = zip(*(image_sizes))

        # 최대 넓이, 전체 높이 
        max_width, total_height = max(widths), sum(heights)

        # 캔버스 
        if img_space > 0: # 이미지 간격 옵션 적용
            total_height += (img_space * (len(images) - 1))

        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
        y_offset = 0 # y 위치
        # for img in images:
        #     result_img.paste(img, (0, y_offset)) # x, y
        #     y_offset += img.size[1]

        for idx, img in enumerate(images): 
            # width가 원본유지가 아닌 경우 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space) 

            progress = (idx + 1) / len(images) * 100 # 실제 percent 정보 계산
            p_var.set(progress)
            progress_bar.update()

        # 포맷 옵션 처리
        file_name = "linked_image" + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("성공", "작업이 완료되었습니다.")
    
    except Exception as err: # 예외처리
        msgbox.showerror("ERROR", err)

# 시작
def start():
    # 각 옵션 값 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    # 이미지 통합 작업
    merge_img()

# 파일 프레임 (파일 추가, 파일 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장 경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # ipady(inner padding y)

btn_dest_path = Button(path_frame, text="가져오기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 기로 넓이 옵션
# *가로 넓이 레이블
lbl_width = Label(frame_option, text="폭", width=8)
lbl_width.pack(side="left", padx=5, pady=5)
# *가로 넓이 콤보
opt_width = ["원본 유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 간격 옵션
# *간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)
# *간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션
# *파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)
# *파일 포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 Bar 프레임
frame_progress = LabelFrame(root, text="진행 상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="종료", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="진행시켜", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False) # X(너비), Y(높이) 값 변경 불가
root.mainloop()