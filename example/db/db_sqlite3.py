import sqlite3

# Connection 생성
conn = sqlite3.connect("data/example.db")

# Cursor 생성
cursor = conn.cursor()

# Table 생성
cursor.executescript(
"""
DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id integer primary key autoincrement,
    name text not null,
    qty integer,
    price real,
    date text
);

DELETE FROM items;
"""
)

# 변경사항 저장
conn.commit()


# Parameterized 방식으로 데이터 추가
sql = "INSERT INTO items (name, qty, price, date) VALUES (?, ?, ?, ?)"
item = ("item1", 10, 2.5, "2020-09-16")
cursor.execute(sql, item)

# 추가한 데이터 확인
sql = "SELECT * FROM items"
cursor.execute(sql)
print(cursor.fetchone())
print()


# Named Placeholder 방식으로 데이터 추가
sql = "INSERT INTO items (name, qty, price, date) VALUES (:name, :qty, :price, :date)"
item = {"qty": 3, "price": 1.2, "name": "item2", "date": "2020-09-16"}
cursor.execute(sql, item)

# 조건으로 데이터 확인
sql = "SELECT * FROM items WHERE name = ?"
search = ("item2",)
cursor.execute(sql, search)
print(cursor.fetchone())
print()



# 한번에 많은 데이터를 추가
sql = "INSERT INTO items (name, qty, price, date) VALUES (?, ?, ?, ?)"
items = [
    ("item3", 4, 3.1, "2020-09-15"), 
    ("item4", 3, 2.5, "2020-09-16"), 
    ("item5", 6, 0.5, "2020-09-17")
]
cursor.executemany(sql, items)

# 데이터 조회
cursor.execute("SELECT * FROM items")
rows = cursor.fetchall()
for row in rows:
    print(row)
print()


# 데이터 수정
sql = "UPDATE items SET name = ? WHERE id = ?"
items = [("item14", 4), ("item15", 5)]
cursor.executemany(sql, items)
print("update count = ", cursor.rowcount)
print()

# 데이터 조회
cursor.execute("SELECT * FROM items")
rows = cursor.fetchall()
for row in rows:
    print(row)
print()


# 데이터 삭제
sql = "DELETE FROM items WHERE price < ?"
cursor.execute(sql, (1,))
print("delete count = ", cursor.rowcount)
print()

# 데이터 조회
cursor.execute("SELECT * FROM items")
for row in cursor:
    print(row)
print()


# 변경사항 저장
conn.commit()

# Connection 닫기
conn.close()
