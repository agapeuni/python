import os
file_path = "data/sample.txt"

# 파일이 존재하면 파일읽기
if os.path.exists(file_path):
    # 파일읽기 모드로 열기
    with open(file_path, "r") as f:
        lines = f.readlines()
        # 개행문자(\n)를 처리
        lines = list(map(lambda s: s.strip(), lines))
        for line in lines:
            print(line)

# 파일이 존재하면 파일삭제
if os.path.exists(file_path):
    os.remove(file_path)
