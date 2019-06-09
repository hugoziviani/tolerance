import client as cli
import server as srv
from _thread import *
import threading



s = srv.SServerBC()
s.connect('', cli.cfg.BCASTPORT)
while True:
    message = input()
    s.send(message)



#c = cli.SClientBC()
#c.connect('', cli.cfg.BCASTPORT)

#while True:
#    var = c.receive()
#    print (var)
    




