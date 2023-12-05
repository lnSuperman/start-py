from xmlrpc.client import ServerProxy

server = ServerProxy("http://127.0.0.1:8084")
print(server.add(1, 1))
