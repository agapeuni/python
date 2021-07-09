import paramiko
import sys

try:
    # open a transport
    hostname, port = "127.0.0.1", 124
    transport = paramiko.Transport((hostname, port))

    # auth
    username, password = "sshuser", "1234"
    transport.connect(username=username, password=password)

    # create client
    sftp = paramiko.SFTPClient.from_transport(transport)

    # mkdir
    try:
        sftp.mkdir("sftp_folder")
    except IOError:
        print("sftp_folder already exists")

    with sftp.open("sftp_folder/README.py", "w") as f:
        f.write("1. This was created by example_paramiko4.py.\n")

    # server write
    with open("dump.sql", "r") as f:
        data = f.read()

    with sftp.open("sftp_folder/sftp_dump.sql", "w") as f:
        f.write(data)

    # local write
    with sftp.open("sftp_folder/README.py", "r") as f:
        data = f.read()

    with open("README.py", "wb") as f:
        f.write(data)

    # close
    sftp.close()
    transport.close()

except Exception as e:
    print("*** Caught exception: %s: %s" % (e.__class__, e))
    try:
        transport.close()
    except:
        pass
    sys.exit(1)
