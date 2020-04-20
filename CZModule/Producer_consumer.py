# -*- coding: utf8 -*-

from threading import Thread
from queue import Queue
import time


class Producer(Thread):
      def __init__(self,args,queue):
          Thread.__init__(self)
          self.args=args
          self.queue=queue

      def read(self):
          self.queue.put(self.args)
          time.sleep(1)
      def run(self):
          self.read()

class Consumer(Thread):
      def __init__(self,queue):
          Thread.__init__(self)
          self.queue=queue

      def pr(self,i):
          print("-----------%s"%i)

      def run(self):
          while True:
                j=self.queue.get()
                if j==-1:
                    break
                self.pr(j)
if __name__=='__main__':
    queue=Queue()
    P=[Producer(i,queue) for i in range(100)]
    C=Consumer(queue)
    for Pthread in P:
        Pthread.start()
    C.start()
    for Pthread in P:
        Pthread.join()
    queue.put(-1)
    C.join()
    print("-------end")




