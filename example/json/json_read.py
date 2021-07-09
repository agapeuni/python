import json
import os
file_path = "data/sample.json"

# 파일이 존재하면 파일읽기
if os.path.exists(file_path):
    # 파일읽기 모드로 열기
    with open(file_path, "r") as f:
        json_data = json.load(f)


print(json_data['items'][0]['Code'])
print(json_data['items'][1]['Name'])
print(json_data['items'][2]['Date'])
print()

print(json_data['items'][3])
print()

print(json_data)
print()
