'''
Author: Khai Fahmi

Description: Simple script to create a test log file
'''

import time, pyb

start = pyb.millis()
while(True):
    ts = pyb.millis() - start
    print(ts)

    # run the model and get the confidence
    trigger = 'cough'
    confidence = 0.9

    f = open('logs.txt', 'a+')
    f.write('{}, {}, {}\n'.format(ts, trigger, confidence))
    f.close()

    pyb.delay(1000)

