import barcode
from barcode.writer import ImageWriter

# 이미지로 생성하려면 ImageWriter를 제공해야 한다.
# 한 권으로 이해하는 IoT 교과서의 ISBN
ean = barcode.get('isbn13', '9788931461534', writer=ImageWriter())

# barcode_1.png 파일이 생성된다.
ean.save('./example/barcode/barcode_1')
