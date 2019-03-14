"""
使用互斥锁实现线程同步
"""
from threading import Lock, Thread

#用threading.Lock对象来代表一个互斥锁 (mutex)
lock = Lock()
# critical 临界资源
some_var = 0


class IncrementThread(Thread):
    def run(self):
        # 读取并修改全局变量
        global some_var
        lock.acquire()
        read_value = some_var
        print("some_var in %s is %d" % (self.name, read_value))
        some_var = read_value + 1
        print("some_var in %s after increment is %d" % (self.name, some_var))
        lock.release()


def use_increment_thread():
    threads = []
    for i in range(50):
        t = IncrementThread()
        threads.append(t)
        t.start()
    for t in threads:
        # 调用该方法的线程将等待直到改Thread对象完成，再恢复运行。
        t.join()
    print("After 50 modifications, some_var should have become 50")
    print("After 50 modifications, some_var is %d" % (some_var,))


if __name__ == '__main__':
    use_increment_thread()
