# 파일 다운로드
import ftplib
import os

STR_226 = "226 Transfer complete."

# FTP 서버 파일
ftp_server_file = "/home/pi/nodejs/node-v11.15.0-linux-armv6l.tar.xz"

# 로컬에 저장할 파일명
local_file = "d:/nodejs/node-v11.15.0-linux-armv6l.tar.xz"

# FTP 서버 접속
with ftplib.FTP("192.168.0.16") as ftp:
    try:
        # FTP 서버 로그인
        ftp.login("pi", "pi")

        with open(local_file, "wb") as fp:
            res = ftp.retrbinary("RETR " + ftp_server_file, fp.write)

        # 다운로드 성공여부 확인
        if not res.startswith(STR_226):
            print("Download failed.")
            if os.path.isfile(local_file):
                os.remove(local_file)
        else:
            print("Download complete.")

    except ftplib.all_errors as e:
        print("FTP error:", e)
        if os.path.isfile(local_file):
            os.remove(local_file)
