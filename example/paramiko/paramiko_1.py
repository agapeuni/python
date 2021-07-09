import paramiko
import time

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect("192.168.0.16", username="pi", password="pi", port="22")

    # 새로운 interactive shell session 생성
    channel = client.invoke_shell()

    # 명령 송신
    channel.send("ls")
    time.sleep(1.0)

    # 결과 수신
    output = channel.recv(65535)
    output = output.decode('cp437')
    print(output)

    client.close()

except Exception as e:
    print("*** Caught exception: %s: %s" % (e.__class__, e))

finally:    
    client.close()
