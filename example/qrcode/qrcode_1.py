import qrcode
img = qrcode.make('https://blog.naver.com/agapeuni')
img.save('./example/qrcode/qrcode_1.png')
