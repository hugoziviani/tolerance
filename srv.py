import socket
import cfg
from _thread import *
import threading
import os, re
import time

print_lock = threading.Lock()
ips = [cfg.NODE0, cfg.NODE1, cfg.NODE2, cfg.NODE3, cfg.NODE4]

# thread fuction
def testConnection():
    resp = []
    for ip in ips:
        resp.append(str(os.popen("ping "+ip).read()))
    return resp

def threaded(c):
    while True:
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')
            # lock released on exit
            print_lock.release()
            break
        # reverse the given string from client
#        data = data[::-1]
        data =  'Ola'
        # send back reversed string to client
        c.send(data)

    # connection closed
    c.close()

def Main():
    host = cfg.NODE0
    port = int(cfg.PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()

#if __name__ == '__main__':
#    Main()

def sobeIp(ip):
    print ("Verificando conexao...")
    sys = "ping -c4 " + ip
    r = "".join(os.popen(sys).readlines())
    #print (r)
    if re.search ("64 bytes from", r):
        print ("Link UP - "+ ip)
        return True
    else:
        print ("Link Down - "+ ip)
        return False
    return False

def verificaHosts(ipsList):
    for ip in ipsList:
        ver = sobeIp(ip)
        if (not ver): continue
        time.sleep(cfg.VERIFICANODESTIME)

def sobeParaTh(ipsList):
    while True:
        global stop_thread
        verificaHosts(ipsList)
        if stop_thread:
            print ('\nSerivço terminado com sucesso')
            break


stop_thread = False
t = threading.Thread(target = sobeParaTh, args = (ips,))

t.start()

stop_thread = True
time.sleep(5)

t.join()



#print(lista)




