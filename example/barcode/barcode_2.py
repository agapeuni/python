from barcode import EAN13
from barcode.writer import ImageWriter

# EAN13의 객체를 생성
my_code = EAN13('9002236311037', writer=ImageWriter())
  
# 바코드를 저장
my_code.save("./example/barcode/barcode_2")

