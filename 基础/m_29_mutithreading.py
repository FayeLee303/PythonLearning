import threading
import time

def job1():
    print("T1 start")
    global A,lock
    # 锁住，acquire和release是配套使用
    lock.acquire()
    for i in range(10):
        A += 1
        print("T1",A)
    # job1完了之后打开锁
    lock.release()

def job2():
    print("T2 start")
    global A, lock
    # 锁住
    lock.acquire()
    for i in range(10):
        A += 10
        print("T2",A)
    # job2完了之后打开锁
    lock.release()

def main():
    # 添加线程
    t1 = threading.Thread(target=job1(),name="T1")
    t2 = threading.Thread(target=job2(),name="T2")
    # 启动线程
    t1.start()
    t2.start()
    # 线程执行完之后才向下执行
    t1.join()
    t2.join()
    print("all done\n")
    # print(threading.active_count()) # 有多少个激活了的线程
    # print(threading.enumerate())
    # print(threading.current_thread())

if __name__ == "__main__":
    # 全局变量
    A = 0
    # Lock 对象
    lock = threading.Lock()
    main()

