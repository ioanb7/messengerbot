import SocketServer
from threading import Thread

class MyMessengerTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())
        #self.finish()

class MyDonalduTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())
        #self.finish()

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 7777

    server = SocketServer.TCPServer((HOST, PORT), MyMessengerTCPHandler)
    t = Thread(target=server.serve_forever())
    t.start()


    HOST2, PORT2 = "127.0.0.1", 8888

    server2 = SocketServer.TCPServer((HOST2, PORT2), MyDonalduTCPHandler)
    t2 = Thread(target=server2.serve_forever())
    t2.start()