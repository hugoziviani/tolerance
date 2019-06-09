import client as cli
import server as srv
from _thread import *
import threading



def sobeServer():
    print('Subindo Thread Server BC')
    global runS
    runS = True
    s = srv.SServerBC()
    s.connect('', cli.cfg.BCASTPORT)
    while runS:
        message = input('Digite a MSG p/ Broadcast:')
        s.send(message)


def sobeClient():
    print('Subindo Thread Cliente BC')
    global runC
    runC = True
    c = cli.SClientBC()
    c.connect('', cli.cfg.BCASTPORT)
    
    while runC:
        var = c.receive()
        print ('SERVER disse: ' + var)
        



tC = threading.Thread(target=sobeClient, args = ())
tS = threading.Thread(target=sobeServer, args = ())

tC.start()
tS.start()
time.sleep(10)
tC.stop()
tS.stop()




