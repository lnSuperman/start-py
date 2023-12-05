from jsonrpclib import ServerProxy

server = ServerProxy("http://127.0.0.1:8085")
print(server.add(1, 1))

