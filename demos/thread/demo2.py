import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")

# 开始线程：Thread-1
# 开始线程：Thread-2
# Thread-1: Thu Dec 17 14:24:32 2020
# Thread-2: Thu Dec 17 14:24:33 2020
# Thread-1: Thu Dec 17 14:24:33 2020
# Thread-1: Thu Dec 17 14:24:34 2020
# Thread-2: Thu Dec 17 14:24:35 2020
# Thread-1: Thu Dec 17 14:24:35 2020
# Thread-1: Thu Dec 17 14:24:36 2020
# 退出线程：Thread-1
# Thread-2: Thu Dec 17 14:24:37 2020
# Thread-2: Thu Dec 17 14:24:39 2020
# Thread-2: Thu Dec 17 14:24:41 2020
# 退出线程：Thread-2
# 退出主线程