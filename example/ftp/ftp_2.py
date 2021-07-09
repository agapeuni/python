import ftplib

# FTP 서버 접속
with ftplib.FTP("192.168.0.16") as ftp:
    try:
        # FTP 서버 로그인
        ftp.login("pi", "pi")

        # 현재 디렉토리
        current_dir = ftp.pwd()
        print(current_dir)
        print()

        # 디렉토리 변경
        ftp.cwd("nodejs")
        
        # 현재 디렉토리
        current_dir = ftp.pwd()
        print(current_dir)
        print()

        # nodejs 디렉터리 목록 표시
        print(ftp.dir())

    except ftplib.all_errors as e:
        print("FTP error:", e)

