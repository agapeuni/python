import pymysql

# Connection 생성
conn = pymysql.Connection(host="192.168.0.3", port=3306,
                          user="root", passwd="1234", db="example")

# Cursor 생성
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 기존의 데이터를 삭제하고 AUTO_INCREMENT를 1로 설정
cursor.execute("DELETE FROM items")
cursor.execute("ALTER TABLE items AUTO_INCREMENT = 1")

# 단일 데이터 추가
sql = "INSERT INTO items (name, qty, price) VALUES (%s, %s, %s)"
item = ("item1", 10, 2.5)
cursor.execute(sql, item)
print(cursor.rowcount, "record inserted, ID:", cursor.lastrowid)
print()

# 멀티 데이터 추가
sql = "INSERT INTO items (name, qty, price) VALUES (%s, %s, %s)"
items = [("item2", 4, 3.1), ("item3", 3, 2.5), ("item4", 6, 0.5)]
cursor.executemany(sql, items)
print("insert count = ", cursor.rowcount)
print()

# 데이터 조회
cursor.execute("SELECT * FROM items")
rows = cursor.fetchall()
for row in rows:
    print(row)
print()

# 데이터 수정
sql = "UPDATE items SET name = %s WHERE id = %s"
items = [("item11", 1), ("item12", 2)]
cursor.executemany(sql, items)
print("update count = ", cursor.rowcount)
print()

# 데이터 조회 (1건)
cursor.execute("SELECT * FROM items")
row = cursor.fetchone()
print(row)

# 데이터 조회
rows = cursor.fetchall()
for row in rows:
    print(row)
print()

# 데이터 삭제
sql = "DELETE FROM items WHERE price < %s"
cursor.execute(sql, (1,))
print("delete count = ", cursor.rowcount)
print()

# 데이터 조회
cursor.execute("SELECT * FROM items")
rows = cursor.fetchall()
for row in rows:
    print(row)
print()

# 데이터 조회 with 페이징
cursor.execute("SELECT * FROM items LIMIT 1, 2")
rows = cursor.fetchall()
for row in rows:
    print(row)
print()

# 변경사항 저장
conn.commit()

# Connection 닫기
conn.close()
