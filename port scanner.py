import socket

ipadd="142.250.67.46" #google.com
commports=[80, 443, 25, 587, 110, 143, 3306, 5432, 27017]
openport=[]

for port in commports:
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    try:
        server.connect((ipadd,port))
        print(f"[+] {port} is open port in {ipadd}")
        openport.append(port)
        server.close()
    except:
        print(f"[-] {port} is closed port in {ipadd}")
        server.close()

print("\n")
print("Open Ports are : -",openport)

#THIS IS MADE BY NIK
#This is for learning purposes and I agree that there could be better port scanners.