
import time
from multiprocessing import Pool

def f(x):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == '__main__':
    t1 = time.time()
    array = [1,2,3,4,5]

    p = Pool()
    result = p.map(f, range(100_0000))
    p.close()
    p.join()
    
    print('Pool took:', time.time()-t1)

    t1 = time.time()
    result = []
    for x in range(100_0000):
        result.append(f(x))

    print('Serial processing took:', time.time()-t1)