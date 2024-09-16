from pymycobot import MyCobot
import time

# Set your comport number 
# or teletype path
mc = MyCobot("COMXX", 115200)
i = 0

# Send robot to home position
mc.send_angles([0, 0, 0, 0, 0, 0], 30)

# Wait for some time until the cobot reaches home position 
time.sleep(5)

# release the servos
mc.release_all_servos()

