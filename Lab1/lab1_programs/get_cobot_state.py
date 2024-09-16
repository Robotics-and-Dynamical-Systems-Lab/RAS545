from pymycobot import MyCobot
import time

# Set your comport number 
# or teletype path
mc = MyCobot("COMXX", 115200)
i = 0

# Send robot to a position with J6 at 90
mc.send_angles([0, 0, 0, 0, 0, 90], 30)

# Wait for some time until the cobot reaches the position 
time.sleep(5)

# get angles of joints and coordinates of the end effector
while i < 10: 
    print("::get_angles() ==> degrees: {}\n".format(mc.get_angles()))
    print("::get_coordinates() ==> coordinates: {}\n".format(mc.get_coords()))
    time.sleep(1)
    i+=1

# Release all servos
mc.release_all_servos()
