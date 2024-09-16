from pymycobot import MyCobot

# Set your comport number 
# or teletype path
mc = MyCobot("COMXX", 115200)

# release servos before.
mc.release_all_servos()