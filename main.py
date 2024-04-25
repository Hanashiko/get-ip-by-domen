import socket, random, time, sys
host = input('server domain: ')
ip = socket.gethostbyname(host)
print(ip)
