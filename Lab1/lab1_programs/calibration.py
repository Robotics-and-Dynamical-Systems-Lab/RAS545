from pymycobot import MyCobot
import time

# Set your comport number 
# or teletype path
mc = MyCobot("COMXX", 115200) # for windows
                              # find for mac or linux

# Manually set cobot at home position i.e. at home position all joint angles should be 0.
"""
write your code here.
"""

# calibrate all joints one by one.
for i in range(1, 7):

    # use the set_servo_calibration() method to calibrate joint servos
    """
    write your code here.
    """
    time.sleep(1)

# Release all the servos
"""
write your code here.
"""