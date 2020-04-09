import socket

serverName = 'localhost'
serverPort = 13000
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('Serveri eshte duke pritur per kerkesa')

while True:
    message = input()
    if len(message)<=0:
        break;
    client.sendto(message.encode("utf-8"),(serverName, serverPort))
    data, address = client.recvfrom(4096)
    print(data.decode())
    if message=='quit':
        break
client.close()

