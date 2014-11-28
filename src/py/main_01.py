import http_server
import message
#import gevent

from multiprocessing import Process

"""

def run ():

    worker_01 = gevent.spawn(http_server.http_run)
    worker_02 = gevent.spawn(message.msg_run)
    print("error...")
    gevent.joinall([worker_01,
                    worker_02]
                )
"""

def proc_run():
    worker_01 = Process( target = http_server.http_run,  )
    worker_01.start()
    print 1
    worker_02 = Process( target = message.msg_run, )
    print 2
    worker_02.start()
    print 3

    #for i in [worker_01, worker_02]:
    #    print(i)
    #    i.start()
        #i.join()


if __name__ =='__main__':
    proc_run()

import time
time.sleep(50)
