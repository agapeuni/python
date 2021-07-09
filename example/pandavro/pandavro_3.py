import pandas as pd
import pandavro

# member 리스트
member = [
    {"name": "유재석", "birth": "1972-08-14", "job": "MC, 개그맨"},
    {"name": "강호동", "birth": "1970-05-11", "job": "MC, 개그맨"},
    {"name": "김구라", "birth": "1970-10-03", "job": "MC, 개그맨"},
]
print(type(member))
print()

# DataFrame
df1 = pd.DataFrame.from_records(member)
print(df1)
print()

# Avro 쓰기
pandavro.to_avro("./data/csv/member.avro", df1)

# Avro 읽기
df2 = pandavro.from_avro("./data/csv/member.avro")
print(df2)
