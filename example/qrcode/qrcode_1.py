import qrcode

# 블로그 URL
img = qrcode.make('https://blog.naver.com/agapeuni')

# 이미지 저장
img.save('./example/qrcode/qrcode_1.png')
