import socket

serverName  = 'localhost'
serverPort  = 13000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverName, serverPort))

mesazhi=''
while True:
    mesazhi = client.recv(128)
    print(mesazhi.decode())
    var = input()
    if len(var)<=0:
        break;
    if var=='quit':
        break
    client.sendall(bytes(var,'UTF-8'))
client.close()