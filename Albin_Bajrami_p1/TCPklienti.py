import socket

serverName  = 'localhost'
serverPort  = 13000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverName, serverPort))

mesazhi=''
while True:
  mesazhi = client.recv(124)
  print(mesazhi.decode())
  var = input()
  client.sendall(bytes(var,'UTF-8'))
  if var=='quit':
    break
client.close()