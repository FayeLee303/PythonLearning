import threading
import time
from queue import Queue

def job(list,queue):
    for i in range(len(list)):
        list[i] = list[i]**2
    # return list
    queue.put(list) #相当于返回

def multithreading():
    q = Queue()
    # 把多个线程放在列表里
    threads = []
    data = [[1,2,3],[2,3,5],[3,5,6]]
    for i in range(len(threads)):
        # 添加线程
        # 对每个线程加载data[i]的列表
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()   #  开启线程
        threads.append(t)   #  加到列表里
    for thread in threads:
        thread.join()   #  加到主线程里
    # 用了join，所有线程运行完了才向下执行
    results = []
    for i in range(4):
        results.append(q.get()) # 从queue里按顺序拿出值加到result里
    print(results)

if __name__ == "__main__":
    multithreading()