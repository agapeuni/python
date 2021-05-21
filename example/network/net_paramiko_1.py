import paramiko
import time

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
cli.connect("192.168.0.16", username="pi", password="pi", port="22")

# 새로운 interactive shell session 생성
channel = cli.invoke_shell()

# 명령 송신
channel.send("ls")
time.sleep(1.0)

# 결과 수신
output = channel.recv(65535)
output = output.decode('cp437')
print(output)

cli.close()
