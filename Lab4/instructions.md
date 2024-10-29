# Laboratory 4: Connecting mycobot pro 600 with its digital twin
This laboratory activity is to connect the mycobot pro 600 with its digital twin and perform robot path planning and verification.

## Pre-requisites
1. Activities of the laboratory 3 must be completed before commencing this laboratory. 
2. Install all software requirements and ensure you have the right hardware to perform the lab. 
3. Read the product parameters of mycobot pro 600 before proceeding with this lab. 
4. Please refer to Elephant Robotics mycobot pro 600 website.
5. Prepare a digital twin of the robot in a software of your choice (See previous labs). You may chose the software based on how you have previously made the digital twin. 

## Literature References
The following are some important resources that will help in developing the knowledge required for the lab:
1. MATLAB: See how to obtain license for MATLAB for ASU students. Instructions to install MATLAB can be found [here](https://ets.engineering.asu.edu/research/software-collaboration-tools/). Scroll down to find MATLAB installation instructions.
2. ROS: See how to install ROS [here](https://wiki.ros.org/ROS/Installation). Learn about ROS from ROS [tutorials](https://wiki.ros.org/ROS/Tutorials)
3. Blender: See how to learn Blender [here](https://docs.blender.org/)
4. Running Python code from MATLAB [here](https://www.mathworks.com/help/matlab/call-python-libraries.html)
5. What are [arUco markers](https://docs.opencv.org/3.4/d9/d6d/tutorial_table_of_content_aruco.html)
6. Check out [OpenCV](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html) to use aruco markers [here](https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html).
7. Check out MATLAB TCP/IP communication [here](https://www.mathworks.com/help/instrument/communicate-using-tcpip-server-sockets.html)


**Must read**: cobot socket programming [here](https://docs.elephantrobotics.com/docs/gitbook-en/2-serialproduct/2.3-myCobot_Pro_600/2.3.5%20socket%20API%20interface%20description.html)

## Laboratory 4 Tasks

1. Complete the homogenous transformations of the cobot pro 600. ( 2 point)

2. Make a digital twin of the cobot pro 600 (3 point)

Warning: Make sure the robot is calibrated !

3. Program the cobot pro 600 using socket programming. (5 points)

   3.1 Connect the pro 600 robot to a monitor, keyboard and mouse.
      
   3.2 Turn on the robot power and log into roboflow OS using the password: elephant.
   
   3.3 Connect the robot to your computer via the ethernet cable. 
   
   3.4 Go to Tools -> Configuration -> Network/Serial Port. Click on Start under the TCP Server section. 
   
   3.5 Bring the robot to the home position using Return to Home function. 
   
   3.6 Execute the python code to send cobot commands. The python code enables your desktop to connect to the robot's IP address. 
   
   3.7 Learn more on how to send cobot commands via Python sockets. A python file is already provided for you [here]()
   
   3.8 You can use any other language to send the cobot commands. 
   
5. Connect the AI kit camera to your computer. (1 marks)

6. Within the workspace place two arUco markers. 

7. Plan the robot path in the digital twin such that the robot moves between the two points in a straight line. (5 marks)

8. Execute the robot path after verifying the robot kinematics in digital twin. (4 marks)


## Upload:

1. Detailed Report with all the equations.
2. All relevant program files of your digital twin.
3. Record a video of the robot operation. 



