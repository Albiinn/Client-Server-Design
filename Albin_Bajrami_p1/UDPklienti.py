import socket

serverName = 'localhost'
serverPort = 13000
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#print("Hello UDP Server, I am client")

while True:
    message = input()
    client.sendto(message.encode("utf-8"),(serverName, serverPort))
    data, address = client.recvfrom(4096)
    print(data.decode())
    if message=='quit':
        break
client.close()

