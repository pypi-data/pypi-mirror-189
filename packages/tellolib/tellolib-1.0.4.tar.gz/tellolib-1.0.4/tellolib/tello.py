import socket

tello_address = ("192.168.10.1", 8889)
pc_address = ("", 8080)

class Tello:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def sendcommand(self, command):
        try:
            command = command.encode()
            sent = self.sock.sendto(command, tello_address)
        except socket.error as msg:
            print("Error sending message: " + str(msg))
            print(str(sent))
    def connect(self):
        try:
            self.sock.bind(pc_address)
            self.sendcommand('command')
        except socket.error as msg:
            print("Failed to bind: " + str(msg))
	