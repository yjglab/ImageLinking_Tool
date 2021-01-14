import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog 
from PIL import Image

root = Tk()
root.title("이미지 연결 도구 v.0.0.1")


# 파일 추가 
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일 선택", \
        filetypes=(\
            ("PNG 파일 (*.png)", "*.png"), ("JPEG 파일 (*.jpg)", "*.jpg"), \
            ("BMP 파일 (*.bmp)", "*.bmp"),  ("모든 파일 (*.*)", "*.*")), \
        initialdir=r"write your directory path") 
       
    
    for file in files:
        list_file.insert(END, file)    

# 선택 삭제
def del_file():
   
    for index in reversed(list_file.curselection()): 
        list_file.delete(index)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "":
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합 
def merge_img():
    try:
        # 가로 넓이 
        img_width = cmb_width.get()
        if img_width == "원본":
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
        
        image_sizes = [] 
        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width * i.size[1] / i.size[0])) for i in images] 
        else:
            image_sizes = [(i.size[0], i.size[1]) for i in images]

        widths, heights = zip(*(image_sizes))

        # 최대 넓이, 전체 높이 
        max_width, total_height = max(widths), sum(heights)

        # 캔버스 
        if img_space > 0: # 이미지 간격 옵션 적용
            total_height += (img_space * (len(images) - 1))

        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
        y_offset = 0 

        for idx, img in enumerate(images): 
            # width가 원본유지가 아닌 경우 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space) 

            progress = (idx + 1) / len(images) * 100 
            p_var.set(progress)
            progress_bar.update()

        # 포맷 옵션 처리
        file_name = "linked_image." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("성공", "작업이 완료되었습니다.")
    except Exception as err:
        msgbox.showerror("ERROR", err)

# 시작
def start():
    # 파일 목록 확인
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

program_name_label = Label(file_frame, pady=3, bg="skyblue", text="Programmed by. Jaegyong Yuk")
program_name_label.pack(side="top", fill="x")

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
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
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) 

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 기로 넓이 옵션
# *가로 넓이 레이블
lbl_width = Label(frame_option, text="폭", width=8)
lbl_width.pack(side="left", padx=5, pady=5)
# *가로 넓이 콤보
opt_width = ["원본", "1024", "800", "640"]
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
opt_format = ["PNG", "JPG", "BMP", "TIFF", "PDF"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 Bar 프레임
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="종료", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, bg="skyblue", padx=5, pady=5, text="진행시켜", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()