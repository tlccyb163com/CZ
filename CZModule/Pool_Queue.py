import time
from multiprocessing import Pool,Manager

def Consumer(Q):
    while True:
          if Q.get()==-1:
               break
          print ("this is Consumer:",Q.get())
    
def Producer(i,Q):
    Q.put(i)

if __name__ == "__main__":
    q=Manager().Queue()
    pool = Pool(processes=3)
    pool.apply_async(Consumer,(q,))
    for i in range(12):
        pool.apply_async(Producer,(i,q))
    
    pool.close()
    pool.join()
    
    print ("all end")
