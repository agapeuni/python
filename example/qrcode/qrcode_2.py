import qrcode

# 파이썬으로 구현하는 디자인 패턴 URL
url_list = (
    'https://blog.naver.com/agapeuni/222260300943',
    'https://blog.naver.com/agapeuni/222260313048',
    'https://blog.naver.com/agapeuni/222260598292'
)

for url in url_list:
    # URL로 QR code 생성
    img = qrcode.make(url)

    # URL에서 '/'를 기준으로 문자열을 나눈다.
    str_array = url.split('/')

    # 블로그 ID를 파일명으로 설정
    img.save('./example/qrcode/qrcode_{}.png'.format(str_array[4]))
