from pymycobot import MyCobot
import time

# Set your comport number 
# or teletype path
mc = MyCobot("COMXX",115200)

# Set cobot at home position.
for i in range(1, 7):
    mc.set_servo_calibration(i)
    time.sleep(1)

mc.release_all_servos()