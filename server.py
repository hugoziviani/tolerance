import socket
import time
import cfg
import os

class SServerBC:
    def __init__(self):
        self.remote_host = self.remote_port = None
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            print('[SBC] - Socket Servidor Broadcast criado !')
        except socket.error:
            print('[SBC] - Falhca na criacao do socket!!')

    def connect(self, remote_host='', remote_port=6969):
        self.remote_host, self.remote_port = remote_host, remote_port
        self.socket.settimeout(0.2)
        self.socket.bind(("", cfg.BCASTSRVRECIVEDATAPORT))
        print('[SBC] - Server: '+ selfIp() +' na porta: '+ str(self.remote_port))

    def send(self, data):
        try:
            self.socket.sendto(data.encode('utf8'), ('<broadcast>', cfg.BCASTPORT))
            print("Mensagem enviada")
            time.sleep(1)
        except:
            print('[SBC] - Dados fora do spectro')

    def receive(self, size = 1024):
        try:
            out = self.socket.recv(size)
            return out.decode('utf8')
        except:
            print('[SBC]-Dados não compatível')
            self.close()

    def close(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
          
def selfIp():
    ip = os.popen('hostname -I').read().replace(' \n', '')
    return ip
