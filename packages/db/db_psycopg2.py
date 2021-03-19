import psycopg2

####################
# DB 생성 및 연결
conn = psycopg2.connect(
    host="localhost", port="5432", user="postgres", password="1234", dbname="postgres"
)

####################
# 커서 생성
cursor = conn.cursor()

# 초기 스크립트
# 기존의 데이터를 삭제하고 자동증가 ID를 1로 설정
cursor.execute("DELETE FROM item_stock")
cursor.execute("ALTER SEQUENCE item_stock_id_seq RESTART WITH 1")

####################
# 단일 데이터 추가
sql = "INSERT INTO item_stock (name, qty, price) VALUES (%s, %s, %s)"
item = ("connector", 10, 2.5)
cursor.execute(sql, item)
print(cursor.rowcount, "record inserted, ID:", cursor.lastrowid)
print()

###################
# 여러 데이터를 한번에 추가
sql = "INSERT INTO item_stock (name, qty, price) VALUES (%s, %s, %s)"
items = [("motor", 4, 3.1), ("circuit", 3, 2.5), ("battery", 6, 0.5)]
cursor.executemany(sql, items)
print("insert count = ", cursor.rowcount)
print()

####################
# 데이터 수정
sql = "UPDATE item_stock SET name = %s WHERE id = %s"
items = [("electric wire", 1), ("servo moter", 2)]
cursor.executemany(sql, items)
print("update count = ", cursor.rowcount)
print()

####################
# 데이터 조회
cursor.execute("SELECT * FROM item_stock")
result = cursor.fetchone()
print(result)

rows = cursor.fetchall()
for row in rows:
    print(row)
print()

####################
# 데이터 삭제
sql = "DELETE FROM item_stock WHERE price < %s"
cursor.execute(sql, (1,))
print("delete count = ", cursor.rowcount)
print()

####################
# 데이터 조회
cursor.execute("SELECT * FROM item_stock")
rows = cursor.fetchall()
for row in rows:
    print(row)

####################
# DB 연결 종료
conn.commit()
conn.close()
