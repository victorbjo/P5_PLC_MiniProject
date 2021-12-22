import socketserver
import waitCalc
waitTimes = open('procssing_times_table.csv')
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        returnedString = str(self.data)
        data = returnedString[2:returnedString.find("</station>")+10]
        wait = waitCalc.getWait(data, waitTimes)
        self.request.sendall(bytes(str(wait)+"\n","utf-8")) 
if __name__ == "__main__":
    HOST, PORT = "172.20.66.43", 11381 #Chan ip to pc ip

    # Create the server, binding to 172.20.66.57 on port 11381
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
