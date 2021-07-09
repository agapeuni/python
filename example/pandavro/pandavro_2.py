import os
import pandavro

df = pandavro.read_avro("./data/csv/example.avro")
print(df)