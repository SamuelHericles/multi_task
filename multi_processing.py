import time
import multiprocessing



square_result = []

def calc_square(numbers):
    global square_result
    print('calc square numbers')
    for n in numbers:
        time.sleep(0.2)
        print('square',n*n)
        square_result.append(n*n)
    print('witihn process result', square_result)

def calc_cube(numbers):
    print('calc cube numbers')
    for n in numbers:
        time.sleep(0.2)
        print('square',n*n*n)


if __name__ == '__main__':
    t = time.time()
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    # p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    # p2.start()

    p1.join()
    # p2.join()


    print('result', str(square_result)) # [] -> each process make a virtual memory so its a new address and new array in each processing
    print('done in',time.time()-t)
    print('......')