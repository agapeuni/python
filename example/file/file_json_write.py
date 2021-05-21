import json
import os

# JSON Data
json_data = {}
json_data['items'] = []

# items 생성
json_data['items'].append({
    "Code": "A1",
    "Name": "item1",
    "Date": "2020-09-19"
})
json_data['items'].append({
    "Code": "A2",
    "Name": "item2",
    "Date": "2020-09-19",
    "Hobby" : ["Tennis", "Cook"]
})
json_data['items'].append({
    "Code": "B1",
    "Name": "item1",
    "Date": "2020-09-20",
    "Memo": {"Hobby1": "Music", "Hobby2": "Movie"}
})
json_data['items'].append({
    "Code": "B2",
    "Name": "item1",
    "Date": "2020-09-20"
})

# 폴더가 없으면 폴더생성
if not os.path.exists("data"):
    os.mkdir("data")

# 파일쓰기 모드로 열기
with open("data/sample.json", "w") as f:
    json.dump(json_data, f, indent=4)
