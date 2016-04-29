import numpy as np

pose_size = 3
net_server = ('166.111.138.128', 8086)
servo_init = np.array((0, 0, 0))
servo_min = np.array((-50, 0, -40))
servo_max = np.array((0, 180, 0))

dummy_point = np.array((30, 90, -35))

# control period
dt = 0.5

