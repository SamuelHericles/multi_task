import time
import multiprocessing

def calc_square(numbers, result,v):
    v.value = 5.67
    for idx, n in enumerate(numbers):
        result[idx] = n*n

if __name__ == '__main__':
    t = time.time()
    arr = [2,3,8,9]
    v = multiprocessing.Value('d', 0.0)
    result = multiprocessing.Array('i',4)
    p1 = multiprocessing.Process(target=calc_square, args=(arr,result,v))

    p1.start()
    p1.join()

    print('19 -result', str(result[:])) 
    print('20 -value', v.value) 
    print('done in',time.time()-t)
    print('......')