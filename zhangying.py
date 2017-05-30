# -*- coding: utf-8 -*-

import socket, threading
import json
SIZE = 1024*500


book_data = None
lib_info = None

def tcplink(sock, addr):
    global book_data, lib_info
    try:
        # 打印连接信息
        print 'Accept new connection from %s:%s...' % addr

        pull_data = sock.recv(SIZE)
        loads_data = json.loads(pull_data)

        if loads_data['head'] == 'android-push':
            book_data = {'book_1':loads_data['book_1'], 'book_2':loads_data['book_2']}
            print book_data

        if loads_data['head'] == 'android-pull':
            sock.send(lib_info)
                         
        if loads_data['head'] == 'rspi':
            lib_info = pull_data
            if book_data != None:
                print '++++++++  send to rspi', book_data
                sock.send(json.dumps(book_data))
                book_data = None
            else:
                sock.send(u'None')
                print '////////////////////'
        
        #print pull_data
        sock.close()
    except Exception, e:
        print e
        print 'hehe, 可能android端json格式不对'



# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口（这里的ip要在不同的情况下更改）
s.bind(('0.0.0.0', 8998))
# 每次只允许一个客户端接入
s.listen(1)
print 'Waiting for connection...'
while True:
    sock, addr = s.accept()
    # 建立一个线程用来监听收到的数据
    t = threading.Thread(target = tcplink, args = (sock, addr))
    # 线程运行
    t.start()
