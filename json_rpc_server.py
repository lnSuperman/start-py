from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def add(a, b):
    return a + b


server = SimpleJSONRPCServer(("localhost", 8085))
server.register_function(add)
server.register_function(lambda x: x, "ping")
server.serve_forever()
