# Laboratory 2: Forward Kinematics of mycobot 280 M5
This laboratory activity is to validate the homogenous transformations of mycobot 280 M5. 

## Pre-requisites
1. Activities of the laboratory 1 must be completed before commencing this laboratory. 
2. Install all software requirements and ensure you have the right hardware to perform the lab. 
3. Read the product parameters of mycobot before proceeding with this lab. 
4. **Warning**: Do NOT exceed the joint angle limits on the cobot. See image below:

<img src="https://github.com/Robotics-and-Dynamical-Systems-Lab/RAS545/blob/fall2024/data/limits.jpeg" alt="image" width="1000" height="300">

## Software Requirements

1. MATLAB: See how to obtain license for MATLAB for ASU students. Instructions to install MATLAB can be found [here](https://ets.engineering.asu.edu/research/software-collaboration-tools/). Scroll down to find MATLAB installation instructions.
2. Python: See how to install Python [here](https://github.com/Robotics-and-Dynamical-Systems-Lab/RAS545/blob/fall2024/Lab1/instructions.md#3-install-python). 
3. pymycobot: See how to install pymycobot in [lab 1 instructions](https://github.com/Robotics-and-Dynamical-Systems-Lab/RAS545/blob/main/Lab1/instructions.md).

## Hardware Requirements
1. mycobot 280 M5 and AI kit setup for programming with Python. See the setup in [Lab 1 instructions](https://github.com/Robotics-and-Dynamical-Systems-Lab/RAS545/blob/main/Lab1/instructions.md).
2. USB Type C cable (Ensure compatibility with your laptop).
3. Any computer with pymycobot installed.

## Laboratory 2 Tasks

1. Find the homogenous transformation matrices between the joint angles of mycobot 280 M5. You may choose your own joint definition axes, but the one present in mycobot [documentation](https://docs.elephantrobotics.com/docs/gitbook-en/2-serialproduct/2.1-280/2.1.6.1-IntroductionOfProductParameters.html) is recommended. 

Enlist the transformation matrices in terms of symbolic theta values i.e. 0H1, 1H2, 2H3, 3H4, 4H5, 5H6. 

2. Perform the product on MATLAB and find the symbolic representation of 0H6 in terms of t0 to t5.

3. Substitute the following values of joint angles from t0 to t5 (i.e. theta0 to theta5) to obtain the position and the orientation of the end effector in MATLAB.

| t0 | t1 | t2 | t3 | t4 | t5 |
|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 0  |
| 20 |-20 | 0  | 0  | 0  | 10 |
| 0  | 0  | 0  | 0  |-20 | 30 |
| 90 | 0  |-90 | 0  | 0  | 10 |

**DIY**: *Students may try alternate combinations of joint angles, and verify them with pymycobot (see point 4)*. 

4. Run the send_angles() method with the arguments as the above joint angles, and then run get_angles() and get_coords(). Do the position and orientation match ? You may use the code templates provided in the [Lab 2 programs folder]https://github.com/Robotics-and-Dynamical-Systems-Lab/RAS545/tree/fall2024/Lab2/lab2_programs).

5. Tabulate your responses and compare the results. Document your code and take screenshots of MATLAB outputs vs pymycobot outputs. Take a video of the operation of the cobot in any one of the above joint angle sets or that of your own.
