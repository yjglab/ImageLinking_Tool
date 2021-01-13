# zip()
kor = ["사과", "포도", "오렌지"]
eng = ["apple", "grapes", "orange"]
print(list(zip(kor, eng))) # [('사과', 'apple'), ('포도', 'grapes'), ('오렌지', 'orange')]

# unzip() : 각 항목에 대해서 첫번째 값끼리, 두번째 값끼리 나눔
mixed = [('사과', 'apple'), ('포도', 'grapes'), ('오렌지', 'orange')]
print(list(zip(*mixed))) # [('사과', '포도', '오렌지'), ('apple', 'grapes', 'orange')]

kor2, eng2 = zip(*mixed)
print(kor2) # ('사과', '포도', '오렌지')
print(eng2) # ('apple', 'grapes', 'orange')