import socket

HOST = 'data.pr4e.org'
PORT = 80

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

while True:
  data = mysock.recv(512)
  if len(data) < 1:
    break
  print(data.decode())
mysock.close()