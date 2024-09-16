from pymycobot import MyCobot
import time

# Set your comport number 
# or teletype path
mc = MyCobot("COMXX", 115200) # for windows
                              # find for mac or linux

# Send robot to a position with Joint 6 at 90 or any position of your choice. 
"""
write your code here.
"""

# Wait for some time until the cobot reaches the position 
time.sleep(5)

# get angles of joints and coordinates of the end effector in a loop for 10 seconds
while i < 10:
    # print the joint angles 
    """
    write your code here.
    """
    
    # Print the end effector coordinates
    """
    write your code here.
    """

    # Wait for one second
    time.sleep(1)
    i+=1

# Release all servos
"""
write your code here.
"""
