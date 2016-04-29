# test 1
# import os
#
# print 'Process (%s) start ...' % os.getpid()
#
# # pid = os.fork()
# for i in range(2):
#     pid = os.fork()
#     if pid == 0:
#         print 'I am child process (%s) and my parent is (%s).--(%s)' % (os.getpid(), os.getppid(), i)
#     else:
#         print 'I (%s) creat a child process (%s).--(%s)' % (os.getpid(), pid, i)
# test 2
# from multiprocessing import Process, Queue
# import os, time, random
#
# # write data
# def write(q):
#     for value in ['A', 'B', 'C']:
#         print 'Put %s to queue...' % value
#         q.put(value)
#         time.sleep(random.random())
#
# # read data
# def read(q):
#     while True:
#         value = q.get(True)
#         print 'Get %s from queue.' % value
#
# if __name__ == '__main__':
#     # create Queue
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # start pw for write
#     pw.start()
#     # start pr for read:
#     pr.start()
#     # wait fot pw stop:
#     pw.join()
#     # pr is a non-stop loop, terminate it
#     pr.terminate()
#
# test 3
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
