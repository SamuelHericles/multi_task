import time
from multiprocessing import Lock, Process, Value


def deposit(balance,lock):
    for i in range(100):
        with lock:
            time.sleep(0.01)
            balance.value = balance.value + 1

def withdraw(balance,lock):
    for i in range(100):
        with lock:
            time.sleep(0.01)
            balance.value = balance.value - 1



if __name__ == '__main__':
    balance = Value('i',200)
    lock = Lock()
    d = Process(target=deposit, args=(balance,lock))
    w = Process(target=withdraw, args=(balance,lock))    

    d.start()
    w.start()

    d.join()
    w.join()

    print(balance.value)