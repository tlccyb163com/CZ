from functools import lru_cache
from datetime import datetime
import time

@lru_cache(maxsize=None)
def fib_cache(n):
    if n < 2:
       return n
    return fib_cache(n-1)+fib_cache(n-2)


def fib_nocache(n):
    if n < 2:
       return n
    return fib_nocache(n-1)+fib_nocache(n-2)


if __name__=="__main__":
    start_cache=time.time()
    print(fib_cache(35))
    end_cache=time.time()

    print ("the fib_cache(35) time is %s"%(end_cache-start_cache))

    start_nocache=time.time()
    print(fib_nocache(35))
    end_nocache=time.time()

    print("the fib_nocache(35) time is %s"%(end_nocache - start_nocache))




