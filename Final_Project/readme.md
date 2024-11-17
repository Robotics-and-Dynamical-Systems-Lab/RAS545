# Final Project: Solving a 4x4 Maze with MyCobot Pro 600

## Pre-Requisites

Before starting this project, ensure the following:

- **Completion of [Lab 4](https://github.com/Robotics-and-Dynamical-Systems-Lab/RAS545/blob/main/Lab4/instructions.md)** is essential to execute this project successfully.
- **MyCobot Pro 600 Digital Twin Setup**: Prepare the digital twin of the MyCobot Pro 600 in your preferred software (e.g., Blender, MATLAB, or ROS). This should have been completed in Lab 4. 
- **Robot Hardware**: Verify the functionality of the physical robot, including proper **calibration**. Learn how to calibrate the robot [here](https://docs.elephantrobotics.com/docs/gitbook-en/2-serialproduct/2.3-myCobot_Pro_600/2.3.4%20development%20environment%20and%20construction.html)
- **Workspace Alignment with ArUco Markers**: You may use ArUco markers to align the workspace. However this is not necessary but it can improve precision of the robot. Learn how to perform camera calibration for ArUco markers with code [here](https://medium.com/@chaitalibh.cb/camera-calibration-with-checkerboard-54f93af742a0). Learn how to detect ArUco markers [here](https://pyimagesearch.com/2020/12/21/detecting-aruco-markers-with-opencv-and-python/).

## Project Objective

The goal of this project is to develop a solution to solve 4x4 rectangular mazes with the **MyCobot Pro 600**. The robot's end effector must navigate through the maze in straight-line sections. A maze will be printed on a plastic board placed within the AI kit's camera zone. The algorithm to solve the maze must automatically determine the entrance, solution path and the exit of the maze. The input to the maze solution algorithm will be an image taken by the AI Kit's camera. The solution path will be consequent straight lines that start at the maze entrance and ends at the maze exit. The solution to the robot's path planning should be visualized in the robot's digital twin before the solution is deployed for execution. The solution algorithm should work for any 4x4 maze generated via the [maze generation tool](https://www.mazegenerator.net/). The robot end effector must autonomously navigate the solution path. 

## Learning Objectives
This project will enable students to learn about robot path planning, image processing and creating an accurate robot digital twin. The challenge in this project is to determine the physical solution of the maze from the image of the maze and produce real-world waypoints for robot navigation. 

## Literature References

Go through all the literature references. They'll be helpful in developing the project. 

- **MATLAB TCP/IP Communication**: [Learn More](https://www.mathworks.com/help/matlab/matlab-engine/tcp-ip-communication.html)
- **ArUco Markers**: [Overview of ArUco Markers](https://www.vision.ee.ethz.ch/en/vision/software/aruco.html)
- **OpenCV for ArUco Detection**: [OpenCV Documentation](https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html)
- Learning Orbis's Robotics playlist for modeling robots in MATLAB. See [here](https://www.youtube.com/playlist?list=PLWF9TXck7O_ymYWT8Q33omPb5K-A5v4Ae)
- Simcape Multibody simulation in MATLAB. See [here](https://www.youtube.com/watch?v=pDiwAA1cnb0&t=2283s)
- Robot forward kinematics in MATLAB. See [here](https://www.youtube.com/watch?v=xpA8TKEMpMk)
- Robot trajectory planning in MATLAB. See [here](https://www.youtube.com/watch?v=Fd7wjZDoh7g)
- What are URDFs. See [here](https://www.youtube.com/watch?v=CwdbsvcpOHM)
- Working with robots in ROS (basics). See [here](https://www.youtube.com/watch?v=2lIV3dRvHmQ&list=PLunhqkrRNRhYYCaSTVP-qJnyUPkTxJnBt)
- Simulating robot kinematics in ROS. See [here](https://www.youtube.com/playlist?list=PLcGRzrc4DaVyt1RLw40FRTNIvHhwIlSNA)
- IKfast Module in ROS is useful to solve inverse kinematics and customize your solution. See [here](https://openrave.org/docs/latest_stable/openravepy/ikfast/#ik-types)
- Creating an IK Fast solution in ROS. See [here](https://wiki.ros.org/Industrial/Tutorials/Create_a_Fast_IK_Solution)
- An approach to solve mazes in MATLAB. See [here](https://www.mathworks.com/matlabcentral/answers/711803-random-maze-solving-algorithm-with-matrix). [Watershed Transform method](https://www.mathworks.com/company/technical-articles/tips-and-tricks-solving-a-maze-with-the-watershed-transform.html). [BFS based maze solver](https://github.com/Mouad4399/-Maze-Solver-In-Matlab-Using-DFS-BFS).
- An approach to solve mazes in Python. See [here](https://thecleverprogrammer.com/2021/01/26/maze-solver-with-python/). Recursivity and A* search see [here](https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/)

## Project Details

### 1: Maze Generation and solving the maze

1a. **Learn about generating a 4x4 Maze**: Use a [maze generation tool](https://www.mazegenerator.net/) to create a 4x4 maze.
   - The maze should have a width and height of 4 cells each.
   - Inner width and inner height of the maze will be 0.
   - The maze can either start at the top or at the bottom **but NOT at the inner room**
   - The E and R values control the maze generation algorithm. They can be anywhere between 0 and 100.
   - Scale and position the maze within the robot’s workspace of **3.5x3.5 inches**.
   - View the [help](https://www.mazegenerator.net/Help.aspx) about the maze generator tool. 
   - Below is a sample image of a randomly generated 4x4 maze starting from the top. 

1b. **Solving the maze**: Students must determine an algorithm to solve the 4x4 maze
   - The algorithm to solve the maze must produce the physical waypoints for navigating the solution path from its image. Hence a physical interpretation of the robot's workspace must be obtained from pixel values of the solution path. 
   - The way points are represented with the numbered green points on the image below. The numbering starts from the top for a maze generated from the top.
   - The number of waypoints would depend on the structure of the maze. 

### 2: Digital Twin Path Planning 

2a. **Digital Twin**: Build a robot digital twin to perform forward and inverse kinematics. You have already done this in Lab 3 and Lab 4.
   - The digital twin should be able to produce end-effector position given the joint angles. 
   - The digital twin should be able to produce realistic joint angles given the end-effector position. 
   - Given a set of end-effector waypoints, the robot's digital twin should be able to move to the waypoints.
   - **important**: It is very important that you perform inverse kinematics and produce realistic joint angles. Directly sending coordinates to the robot is **strictly prohibited**. 

2b. **Path Planning**: Plan the robot's end-effector path to solve the maze.
   - The digital twin should normally be at a home position close to the plastic board but shouldn't obstruct the view of the camera. 
   - The start position of the robot can be either top or bottom (decided by the examiner).
   - After finishing the maze, the robot must return to the home position.

### 3: Execution and Recording

3a. **Setup the system**: 
   - Setup the AIKit in a desired position.
   - Connect the AIkit camera to your computer. 
   - Connect the robot to your computer using **Ethernet**.
   - Follow the [setup process](https://docs.elephantrobotics.com/docs/gitbook-en/2-serialproduct/2.3-myCobot_Pro_600/2.3.5%20socket%20API%20interface%20description.html) to enable socket programming. 
   
3b. **Socket Programming**: 
   - Write a program to perform the waypoint navigation. Socket programming is independent of the programming language. Sample programs for Python and MATLAB are available [here](https://github.com/Robotics-and-Dynamical-Systems-Lab/RAS545/tree/fall2024/Lab4)
   - Make sure to set a speed to navigate the maze in a reasonable time.
   - Execute your program.
   - Ensure the robot follows the waypoints accurately in line as straight as possible. Cross-check with the digital twin.

3c. **Video Recording**:
   - Record a video of your demonstration without fail.

## Demonstration Judgement Criteria

- At a minimum, it should be possible to see the state of the robot at different waypoints in the digital twin. 
- Physical robot movements must be alike to the digital twin.
- End effector must always maintain a safe distance vertical distance from the plastic board. (ideally between 10 to 20 centimeters).
- End effector should follow a path as straight as possible, and should be similar to the expected solution path.
- Your ingenuity of the maze solution approach is very important. There are several ways to solve the maze. Your code should work for all 4x4 rectangular mazes.
- In addition to the above points, students will be judged on the basis of how efficiently they solve the problem. 
- The reliability and robustness of the solution also matters especially when determining physical solutions by processing the image of the maze.
- It is not necessary, but you should build fail-safes into your solution. For example: you could use a the escape key to make the robot return to a safe home position.

## Submission Requirements

- **Report**: Detailed report covering the methodology, challenges, solutions, and outcomes.
- **Code Files**: Submit all code files used for path planning, execution, and robot control (MATLAB .m files/Simulink slx files/ urdfs/ xmls / python files /ros related files etc.).
- **Video**: A video demonstrating the robot solving the maze.

## Grading Breakdown
Total: 30 points
- **Submission Requirements**: 15 points
    - report: 5 points
    - code files: 5 points
    - video: 5 points
- **Demonstration**: 15 points
    - digital twin: 10 points
    - physical operation of the robot: 5 points


## Best Practises

- Go through all the literature references. 
- Pre-determine a position to keep the AIkit during demonstration.
- Record all information you need beforehand. 
- Write error-proof code. 
- Do not copy from others. Mistakes might cost you. 
- Take printouts of the maze and test your algorithm several times on various 4x4 mazes. 
- Operate the robot with care. Always ensure that your teammate assists in stopping the robot during emergency. 
- Test the digital twin's results manually before running the socket program. 
- Make sure to wait for the robot to complete the previous command before executing the next. Make use of the wait_command_done() command. Failing to do so might cause the robot to malfunction. 
- Align the camera properly and perform camera calibration to avoid errors due to camera distortion. 
- Try avoiding the camera stand while maneuvering the robot. 
- Manage your time. Almost all of the work can be performed in the digital twin. 
- Ensure to record your demonstration. As the number of attempts are limited due to semester end deadline, you may not get a chance to record the video if your forget to do so during demonstration.

## Frequently Asked Questions (FAQs)

**Q. Is it expected that the AIKit will be moved during demonstration ?**\
Ans. No. The AIKit can be kept fixed. The student team can decide where to fix the AIKit. We suggest to keep it conveniently inside the workspace of the robot such that the robot doesn't collide with itself.

**Q. Is it expected that the white plastic plate will be moved during demonstration ?**\
Ans. No. Unlike lab 4, the white plastic plate will be placed in the camera zone. The students only need to demonstrate once on the robot. However the start position (top or bottom) will be decided by the examiner. 

**Q. Will there be a theory viva ?**\
Ans. No. There will be no theory viva. However, some general lab-related questions may be asked. 

**Q. Is it required for the digital twin to move in real-time ?**\
Ans. No. But it should at least produce the joint-angles for the way-points. 

**Q. How accurate should the robot movement be ?**\
Ans. The end effector should roughly point on white region of the maze while navigating through the solution path. It is not expected to avoid collision with the maze but the robot movement must bear similarity to the expected solution path. 

**Q. What approach should I use to solve the maze?**\
Ans. This is a graduate class. Use any approach to solve the maze. There's some help available in the Literature Reference section to guide you. However, it is your choice on how to solve the maze. You will be judged on the basis of your approach. 

**Q. How fast should the robot move?**\
Ans. The end effector movement should be at a speed such that the maze is completed at a reasonable time. Keep the speed parameter between 300 - 500. 

**Q. Can I chose my own 4x4 maze and perform demonstration ?**\ 
Ans. No. A random 4x4 maze will be provided to you with a start position decided by the examiner. It is expected that you produce a maze solution algorithm that works for all 4x4 mazes. Here are some [sample 4x4 mazes](). The 4x4 mazes provided in the demonstration will be similar. It is recommended that you take a print of the sample mazes for testing your solution. 

**Q. For the project, is it necessary to use ArUco markers ?**\
Ans. No. Since the AIKit and the plastic board are kept fixed, it is not necessary to use ArUco markers. The camera zone can be mapped even without using ArUco markers. However, using ArUco markers can help in accurately mapping the camera zone. 

**Q. Why is my ArUco marker not getting detected properly ?**\
Ans. It is likely because you haven't performed camera calibration. Every camera has some sort of distortion due to the lens' focal length and aperture. Camera calibration is performed to compensate for the distortion.

**Q. How will the demonstration be scored ?**\
Ans. Demonstration is scored by following the judgement criteria. The demonstration is subjectively judged. 

**Q. How can I ensure to get a full score ?**\
Ans. The minimum requirement to get a full score in the demonstration is to produce a correct solution of the maze and execute it perfectly (both in the digital twin and in reality). To get a full score in the documentation, please ensure that the submission requirements are strictly followed.

**Q. Will there be partial credit ?**\
Ans. Yes. This is reviewed on case to case basis. 

**Q. What happens if I am unable to produce a satisfactory demonstration and time runs out ?**\
Ans. As the semester end deadline is nearing, the number of demonstration attempts are limited. if you are unable to produce a satisfactory demonstration, then you will be graded partially on the basis of the performance of the latest demonstration. 

**Q. When do I submit the project on canvas ?**\
Ans. Every student must individually submit all necessary files (mentioned in the submission requirements) by the deadline posted on canvas regarless of a satisfactory demonstration. Remember that the submission files require you to document and record your demonstration. So submitting a report with incomplete/no demonstration will lead to further loss of score. 
