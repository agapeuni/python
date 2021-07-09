# 파일 업로드
import ftplib

STR_226 = "226 Transfer complete."

# 로컬 파일
local_file = "d:/nodejs/node-v11.15.0-linux-armv6l.tar.xz"

# FTP 서버 
ftp_server_file = "/home/pi/node.tar.xz"

# FTP 서버 접속
with ftplib.FTP("192.168.0.16") as ftp:
    try:
        # FTP 서버 로그인
        ftp.login("pi", "pi")

        with open(local_file, "rb") as fp:
            res = ftp.storlines("STOR " + ftp_server_file, fp)

            # 업로드 성공여부 확인
            if not res.startswith(STR_226):
                print("Upload failed")
            else:
                print("Upload complete.")

    except ftplib.all_errors as e:
        print("FTP error:", e)
