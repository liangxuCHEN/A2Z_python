from multiprocessing import Process
import os
import time

# 子进程要执行的代码
def run_proc(name):
    time.sleep(10)
    print('运行子进程 %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    p = Process(target=run_proc, args=('test',))
    print('开启父进程.')
    p.start()
    print('父进程 %s.' % os.getpid())
    p.join()
    print('子进程结束.')