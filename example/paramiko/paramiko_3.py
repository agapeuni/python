import paramiko

try:

    transport = paramiko.Transport("192.168.0.16", 22)
    transport.connect(username="pi", password="pi")

    sftp = paramiko.SFTPClient.from_transport(transport)

    # download
    sourcefilepath = 'uploadExam.txt'  # SFTP 패스 내 다운로드 할 파일 경로
    localpath = 'downloadExam.txt'  # workspace 경로 내 다운로드 경로 및 파일명

    sftp.get(sourcefilepath, localpath)

    # close
    sftp.close()
    transport.close()

except Exception as e:
    print("*** Caught exception: %s: %s" % (e.__class__, e))

finally:
    transport.close()