# -*- coding: utf-8 -*-

import socket
import json


import time
remote_socket = ('47.93.193.169',8998)
push_data = {'head':'android-push', 'book_1':0, 'book_2':1}

def android_sim_push():
    global remote_socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(remote_socket)
    s.send(json.dumps(push_data))
    s.close()

    
pull_data = {'head':'android-pull'}
def android_sim_pull():
    global remote_socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(remote_socket)
    s.send(json.dumps(pull_data))
    info = s.recv(1024)
    print 'lib info = ', info
    s.close()


android_sim_push()

time.sleep(1)
android_sim_pull()

