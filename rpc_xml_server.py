from xmlrpc.server import SimpleXMLRPCServer


class Calculate:

    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x * y

    def sub(self, x, y):
        return abs(x - y)

    def div(self, x, y):
        return x / y


if __name__ == '__main__':
    obj = Calculate()
    server = SimpleXMLRPCServer(("", 8084))
    server.register_instance(obj)
    print("服务启动")
    server.serve_forever()
