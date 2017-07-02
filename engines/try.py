# #! encoding: utf-8
#
# import os
# import signal
# from time import sleep
#
#
# def onsignal_term(a, b):
#     print '收到SIGTERM信号'
#
#
# # 这里是绑定信号处理函数，将SIGTERM绑定在函数onsignal_term上面
# signal.signal(signal.SIGTERM, onsignal_term)
#
#
# def onsignal_usr1(a, b):
#     print '收到SIGUSR1信号'
#
#
# # 这里是绑定信号处理函数，将SIGUSR1绑定在函数onsignal_term上面
# signal.signal(signal.SIGUSR1, onsignal_usr1)
#
# while 1:
#     print '我的进程id是', os.getpid()
#     sleep(10)

# player = {-1: "Black", 1: "White"}
# player[-1] = player[-1][:-8]
# player[1] = player[1][:-8]
#
# print player
# for x in xrange(8):
#     for y in xrange(8):
#         print "priority[(",x,",",y,")] = 0"
priority = {}
priority[( 0 , 0 )] = 6
priority[( 0 , 1 )] = 1
priority[( 0 , 2 )] = 5
priority[( 0 , 3 )] = 5
priority[( 0 , 4 )] = 5
priority[( 0 , 5 )] = 5
priority[( 0 , 6 )] = 1
priority[( 0 , 7 )] = 6
priority[( 1 , 0 )] = 1
priority[( 1 , 1 )] = 0
priority[( 1 , 2 )] = 2
priority[( 1 , 3 )] = 2
priority[( 1 , 4 )] = 2
priority[( 1 , 5 )] = 2
priority[( 1 , 6 )] = 0
priority[( 1 , 7 )] = 1
priority[( 2 , 0 )] = 5
priority[( 2 , 1 )] = 2
priority[( 2 , 2 )] = 4
priority[( 2 , 3 )] = 4
priority[( 2 , 4 )] = 4
priority[( 2 , 5 )] = 4
priority[( 2 , 6 )] = 2
priority[( 2 , 7 )] = 5
priority[( 3 , 0 )] = 5
priority[( 3 , 1 )] = 2
priority[( 3 , 2 )] = 4
priority[( 3 , 3 )] = 3
priority[( 3 , 4 )] = 3
priority[( 3 , 5 )] = 4
priority[( 3 , 6 )] = 2
priority[( 3 , 7 )] = 5
priority[( 4 , 0 )] = 5
priority[( 4 , 1 )] = 2
priority[( 4 , 2 )] = 4
priority[( 4 , 3 )] = 3
priority[( 4 , 4 )] = 3
priority[( 4 , 5 )] = 4
priority[( 4 , 6 )] = 5
priority[( 4 , 7 )] = 2
priority[( 5 , 0 )] = 5
priority[( 5 , 1 )] = 2
priority[( 5 , 2 )] = 4
priority[( 5 , 3 )] = 4
priority[( 5 , 4 )] = 4
priority[( 5 , 5 )] = 4
priority[( 5 , 6 )] = 2
priority[( 5 , 7 )] = 5
priority[( 6 , 0 )] = 1
priority[( 6 , 1 )] = 0
priority[( 6 , 2 )] = 2
priority[( 6 , 3 )] = 2
priority[( 6 , 4 )] = 2
priority[( 6 , 5 )] = 2
priority[( 6 , 6 )] = 0
priority[( 6 , 7 )] = 1
priority[( 7 , 0 )] = 6
priority[( 7 , 1 )] = 1
priority[( 7 , 2 )] = 5
priority[( 7 , 3 )] = 5
priority[( 7 , 4 )] = 5
priority[( 7 , 5 )] = 5
priority[( 7 , 6 )] = 1
priority[( 7 , 7 )] = 6

for x in xrange(7,-1,-1):
    print x

import time
print time.time()