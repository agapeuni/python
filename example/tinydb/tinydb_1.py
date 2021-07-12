from tinydb import TinyDB, Query
db = TinyDB("./data/example.tinydb")

db.drop_table("books")
table = db.table("books")

# 데이터 삽입
table.insert({"name": "파이썬", "price": 24000})
table.insert({"name": "텐서플로", "price": 17000})
table.insert({"name": "케라스", "price": 18000})

# 데이터 조회
list = table.all()
print(list)
print()

Book = Query()

# name이 '텐서플로'인 데이터 검색
rs = table.search(Book.name == "텐서플로")
print(rs[0]["price"])
print()

# price가 18000원 이상인 데이터 검색
rs = table.search(Book.price >= 18000)
for item in rs:
    print(item["name"])
print()

# 파이썬 price를 수정
table.update({'price': 20000}, Book.name == '파이썬')
list = table.all()
print(list)

# 2만원미만 삭제
table.remove(Book.price < 20000)
list = table.all()
print(list)
