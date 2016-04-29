import socket, time
import parameters as pms
import numpy as np
import string

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(pms.net_server)
print 'connect success'
servo = pms.servo_init
catch = 0
try:
    while True:
        start = time.time()
        pose = np.hstack([1, servo, catch])

        message = ','.join(['%s' % pose[i] for i in range(len(pose))])
        print 'pose  : ' + message
        s.send(message)
        message = s.recv(1024)
        print 'action: ' + message
        temp = message.split(',')
        action = [string.atof(temp[i]) for i in range(len(temp))]

        servo = np.vstack([action[1:-1], pms.servo_min]).max(0)
        servo = np.vstack([servo, pms.servo_max]).min(0)
        if action[-1] == 1:
            delta = servo - pms.dummy_point
            servo = pms.servo_init
            if delta.dot(delta) < 5*5:
                catch = 1
        else:
            catch = 0
        end = time.time()
        dt = max(pms.dt+start-end, 0)
        time.sleep(dt)
        print 'Run %0.2f seconds.' % (end - start)
finally:
    s.close()
    print 'socket close success'


