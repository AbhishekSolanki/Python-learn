import socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind(("localhost",8001))
skt.listen(10)
print 'Socket now listening'  
skt.close()
print 'Socket closed'  
