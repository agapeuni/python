import ftplib

# FTP 서버 접속
with ftplib.FTP("192.168.0.16") as ftp:
    try:
        # FTP 서버 로그인
        ftp.login("pi", "pi")

        # Webcome Banner 표시
        print(ftp.getwelcome())
        print()

        # 홈디렉터리 목록 표시
        print(ftp.dir())

    except ftplib.all_errors as e:
        print("FTP error:", e)
