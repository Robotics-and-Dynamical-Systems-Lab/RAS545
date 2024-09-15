# Laboratory 1: Introduction to mycobot

[mycobot series](https://www.elephantrobotics.com/en/mycobot-en/) robots are 6-axis entry level collaborative robots from [elephant robotics](https://www.elephantrobotics.com/en/) supported on multiple platforms. 
It can be interfaced with Python/C++/C#/JavaScript. mycobot also provides ROS packages, control via serial communication, and development with Arduino. Refer to [mycobot gitbook](https://docs.elephantrobotics.com/docs/gitbook-en/) 
Mycobot comes with [MyStudio](https://docs.elephantrobotics.com/docs/gitbook-en/4-BasicApplication/4.1-myStudio/), a one-stop GUI platform for maintenance of cobot firmware. 
[Basic]() is burnt on to mycobot base using mycobot.exe and Atom is flashed onto Atom main.
This laboratory uses pymycobot API for interacting with the robot in Python. pymycobot can be installed from [github](https://github.com/elephantrobotics/pymycobot) or directly via pip.
This lab will use [mycobot 280](https://shop.elephantrobotics.com/collections/mycobot-280) with the M5 Stack.

This lab activity introduces programming the cobot with Python and enables the understanding of the robot's joint orientations and control.

## Software Requirements
1. MyStudio
2. MyStudio Firmware (Basic and Atom)
3. Python
4. Anaconda or Miniconda (Optional)

## Hardware Requirements
1. mycobot 280 M5 and AI kit
2. USB Type C cable (Ensure compatibility with your laptop).
3. Any computer or a laptop with 10 GB of free harddisk memory.

## Setup your cobot system

### 1. MyStudio
The mycobot 280 M5 is based on the [M5 development stack](https://github.com/m5stack). MyStudio is a comprehensive for all cobot firmware burning, documentation, tutorials.
MyStudio is available on Windows and Mac x86_64 builds, and can be downloaded from its github release. MyStudio app image is unavailable for linux x86_64 builds. Hence for first time setup, use a Windows/Mac x86_64 build to flash the firmware into the robot. Firmware flashing is a one-time process, and is independent of the OS being used to flash it. Once flashed, a user can use Windows/Mac/Linux to program the robot. 
 
MyStudio installer can be downloaded from [github](https://github.com/elephantrobotics/myStudio) or from its [webpage](https://www.elephantrobotics.com/myCobot/#myStudio).
Use a usb type C cable to connect the M5 stack with the cobot (as shown in the picture below).

![image](https://github.com/Robotics-and-Dynamical-Systems-Lab/RAS545/blob/fall2024/data/usb.jpeg)

Run installer as administrator and allow prompts from firewall for installing. After installation open the Basic section (shown below). 

![image](https://github.com/Robotics-and-Dynamical-Systems-Lab/RAS545/blob/fall2024/data/basic.jpeg)

The software should automatically detect the cobot version and the USB port. If not select it manually and click login. 
The USB port number can be found in device manager in Windows or System Report in Mac.  

Here's an image of how the comports should look:

![image](https://github.com/Robotics-and-Dynamical-Systems-Lab/RAS545/blob/fall2024/data/image.png)

Note down the terminal to which the cobot is connected. Select language as English, Location as "other regions" and click login.


**Side Note:**\
If you'll be using a linux machine after flashing, run the following command to enlist all terminals.

```
sudo dmesg | grep tty
```

or enlist all teletype terminals via the command:

```
cd ~
```

```
ls /dev/tty*
```

The name of the terminal can be identified from this list.

### 2. Flashing the firmware

**2a. Flashing Atom**\
Connect the usb cable to the USB port in the robot's end effector 

Go to AtomMain in Basic section in MyStudio. Download the latest firmware and burn Atom.

**2b. Flashing Basic**\
Click on this [link](https://github.com/elephantrobotics/myCobot/releases/download/0/myCobot._windows_x64.zip), to download Basic Flasher for Windows. 
Connect the USB cable to the cobot's M5 Stack as shown in the first image:

Extract the Basic Flasher zip file. In the firmware selection, select "Transponder". The Terminal should be Basic and Port should be COMPORT to which the robot is connected to.
See image below:

![image](https://github.com/Robotics-and-Dynamical-Systems-Lab/RAS545/blob/fall2024/data/transponder.png)

Click burn to flash the Basic Firmware into M5 Stack.

After completing the above steps, your cobot is ready to be programmed via Python. 

### 3. Install Python 

MyCobot can be interfaced with Python via the pymycobot API. If you do not have Python installed in your system follow the steps below:

#### 3a. Install via environment manager (Recommended)

Anaconda Installation Instructions

#### Install Anaconda on Windows/Mac

1. **Download the Installer**:
   - Visit the [Anaconda Downloads Page](https://www.anaconda.com/products/distribution#download-section).
   - Choose the **Windows** version and download the installer (usually `.exe`).

2. **Run the Installer on Windows/Mac**:
   - Double-click the downloaded `.exe` file to launch the installer.
   - Follow the prompts in the setup process.
   - **Check** the option to add Anaconda to your PATH environment variable (optional but recommended).

   If you are on a linux machine, open a terminal and navigate to the directory where the `.sh` file is located. Then, run the following command:
   ```
   bash Anaconda3-*.sh
   ```

**Note:** Skip for Steps 3 if you are using Windows.

3. **Configure the Shell**:
   If you are on Mac, If you’re using **zsh** (the default on macOS Catalina and later) or **bash**, add Anaconda to your shell profile by running:

   ```
   echo 'export PATH="~/anaconda3/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

   If you are on ubuntu using bash: 

   ```
   echo 'export PATH="~/anaconda3/bin:$PATH"' >> ~/.bash_profile
   source ~/.bash_profile
   ```

4. **Complete the Installation**:
   - After installation, you can open the **Anaconda Navigator** from the Start Menu in Windows.
   - On linux, open a new terminal after installation to start anaconda.
   - You can also use the **Anaconda Prompt** to run commands like `conda` and `python`.

5. **Verify Installation**:
   Open a command prompt and run:

   ```
   conda --version
   ```

6. Install Python in new environment
   Open a command prompt and activate conda

   ```
   conda activate base
   ```

   ```
   conda create --name myenv python=3.10
   ```

   Enter the desired name of your environment instead of myenv. 

   ```
   conda activate myenv
   ```

#### 3a. Native installation (Not Recommended)

You may install Python natively, but this is not recommended, as environment managers allow for isolation of dependencies to avoid conflicts with other tools .

#### 1. Install Python on Windows

1. **Download the Installer**:
   - Visit the [Python Downloads Page](https://www.python.org/downloads/).
   - Choose the **Windows** version and download the latest `.exe` installer.

2. **Run the Installer**:
   - Double-click the downloaded `.exe` file to start the installation.
   - **Important**: Check the box that says "Add Python to PATH" at the bottom of the installer window.
   - Choose **Install Now** or **Customize Installation** if you want to specify installation options.

3. **Complete the Installation**:
   - Follow the prompts to finish the installation.

4. **Verify Installation**:
   - Open a command prompt and run the following command to verify the installation:

   ```
   python --version
   ```

This should display the installed version of Python.


#### 2. Install Python on macOS

1. **Download the Installer** :
   - Visit the [Python Downloads Page](https://www.python.org/downloads/).
   - Choose the **macOS** version and download the `.pkg` file for the latest Python release.

2. **Run the Installer** :
   - Double-click the downloaded `.pkg` file to start the installation.
   - Follow the installation prompts.

3. **Update Shell Profile** (Optional):
   If the installed Python version is not the default version, you can update your shell profile.
   For **zsh** (default on macOS Catalina and later):

   ```
   echo 'export PATH="/usr/local/bin/python3:$PATH"' >> ~/.zshrc 
   ```

   ```
   source ~/.zshrc
   ```

#### 3. Install Python on linux

1. Open a terminal and run the following commands based on your distribution:

- **For Ubuntu/Debian**:
```
sudo apt update
sudo apt install python3 python3-pip
```
   
- **For Fedora**:

```
sudo dnf install python3
```

- **For Arch Linux**:

```
sudo pacman -S python
```

2. Configure Environment (Optional):
If needed, you can configure your shell to use `python3` as the default Python version by creating an alias:

```
echo 'alias python=python3' >> ~/.bashrc
```
source bashrc.
```
source ~/.bashrc
```

**4. Install pymycobot**

```
pip install pymycobot
```


## Test your system

First check if you have the right packages by listing them: 

```
pip list
```


Perform the following tasks to complete your lab demonstration:

### 1. Calibrate your robot
### 2. Move the cobot

