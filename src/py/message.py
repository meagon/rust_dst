
#from gevent_zeromq import zmq
import time  
import zmq



def msg_run():
    print 4
    context = zmq.Context()  
    socket = context.socket(zmq.REP)  
    print("prep for bind ...")
    socket.bind("tcp://*:5555") 
    print("conn  at port 5555")
    while True:  
        #  Wait for next request from client  
        #message = socket.recv_pyobj() 
        message = socket.recv() 
        if message == 'quit': 
            print("exiting ...")
            break
        print "Received request: ", message  
        time.sleep (1)        #   Do some 'work'  
        #  Send reply back to client  
        socket.send("World") 
