import pymongo

####################
# DB 생성 및 연결
# conn = pymongo.MongoClient("localhost", 27017)
conn = pymongo.MongoClient("mongodb://root:1234@192.168.0.3:27017/")

"""
username = 'test'
password = '1234'
conn = pymongo.MongoClient('mongodb://%s:%s@localhost' % (username, password))
"""

####################
# Database 생성
mongo_db = conn["example"]
# mongo_db = conn.example

####################
# Collections 생성
mongo_col = mongo_db["items"]
# mongo_col = mongo_db.items

####################
# 초기 실행 코드
# mongo_col.delete_many({})

####################
# 단일 데이터 추가
print("insert_one")
data = {"name": "connector", "qty": 10, "price": 2.5}
x = mongo_col.insert_one(data)
print("record inserted, ID:", x.inserted_id)
print()

####################
# 여러 데이터 추가
print("insert_many")
data_dic = [
    {
        "name": "motor",
        "qty": 4,
        "price": 3.1,
        "country": "china",
        "memo": "bad quality",
    },
    {
        "name": "circuit",
        "qty": 3,
        "price": 2.5,
        "country": "japan",
        "stock": 0,
        "info": "regulated item",
    },
    {"name": "battery", "qty": 6, "price": 0.5, "country": ["korea", "china"]},
]

x = mongo_col.insert_many(data_dic)
print("record inserted, IDs:", x.inserted_ids)
print()

print("count = ", mongo_col.count())

####################
# 데이터 수정
print("update_one")
mongo_col.update_one({"name": "moter"}, {"$set": {"name": "servo moter"}})

####################
# 데이터 조회
rows = mongo_col.find()
for row in rows:
    print(row)
print()

####################
# 데이터 조회 with 조건
print("find qty > 5")
my_query = {"name": {"$in": ["connector", "motor", "circuit"]}}
rows = mongo_col.find(my_query)
for row in rows:
    print(row)
print()

####################
# 데이터 삭제
print("delete_many price < 3")
mongo_col.delete_many({"price": {"$lt": 3}})

"""
$eq = Matches values that are equal to a specified value.
$gt > Matches values that are greater than a specified value.
$gte >= Matches values that are greater than or equal to a specified value.
$in Matches any of the values specified in an array.
$lt < Matches values that are less than a specified value.
$lte <= Matches values that are less than or equal to a specified value.
$ne != Matches all values that are not equal to a specified value.
$nin Matches none of the values specified in an array.
"""

####################
# 데이터 조회
rows = mongo_col.find()
for row in rows:
    print(row)
print()
