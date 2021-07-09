import paramiko

transport = paramiko.Transport("192.168.0.16", 22)
transport.connect(username="pi", password="pi")

sftp = paramiko.SFTPClient.from_transport(transport)

# upload
sourcefilepath = 'example.txt'  # WorkSpace 경로 내 업로드할 파일 경로
localpath = 'uploadeExam.txt'  # SFTP 패스 내 저장될 경로 및 파일명

sftp.put(sourcefilepath, localpath)

# close
sftp.close()
transport.close()
