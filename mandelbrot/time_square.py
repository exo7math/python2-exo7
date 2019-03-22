import time
import math

def timeit1():
    s = time.time()
    for i in range(1000000):
        z=(i/3)**2
    print("Took %f seconds" % (time.time() - s))

def timeit2(arg=math.sqrt):
    s = time.time()
    for i in range(1000000):
        z=(i/3)*(i/3)
    print("Took %f seconds" % (time.time() - s))

timeit1()
timeit2()