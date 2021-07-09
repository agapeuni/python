import os

# 폴더가 없으면 폴더생성
if not os.path.exists("data"):
    os.mkdir("data")

# 파일쓰기 모드로 열기
with open("data/sample.txt", "w") as f:
    for i in range(1, 21):
        line = "line %d. " % i
        f.write(line + "This is sample file\n")
        
