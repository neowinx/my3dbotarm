# my3dbotarm
ROS Packages for 3DArm+ https://www.thingiverse.com/thing:4023371

# Requirements

- [ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu) - http://wiki.ros.org/melodic/Installation/Ubuntu
- [Moveit](https://moveit.ros.org/install/) - https://moveit.ros.org/install/
- [Arduino IDE](https://www.arduino.cc/en/Main/Software) **(in the same host where you've installed ROS)** - http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup
- [rosserial_arduino](http://wiki.ros.org/rosserial_arduino) - http://wiki.ros.org/rosserial_arduino
- [Git](https://git-scm.com/) - https://git-scm.com/

# Installation

## Prepare Arduino IDE and ros_lib

```bash
sudo apt-get install ros-melodic-rosserial
sudo apt-get install ros-melodic-rosserial-arduino
cd ~/sketchbook/libraries/
```

## Prepare catkin_ws and code

```bash
mkdir ~/catkin_ws
cd ~/catkin_ws
git clone https://github.com/neowinx/my3dbotarm.git src
```

## Upload code to arduino

```bash
arduino ~/catkin_ws2/src/my3dbotarm_code_arduino/my3dbotarm_code_arduino.ino
```

# Usage

## Open moveit in one terminal
```bash
roslaunch my3dbotarm_moveit_config demo.launch
```

## Launch rosserial in another terminal
```bash
./rosserial_init.sh
```

## Open my3dbotarm_description rviz.launch

If you want to open rviz with the launch file provided in **my3dbotarm_descripcion/launch/rviz.launch** you will need to install the **ros-melodic-joint-state-publisher-gui** package before

```bash
sudo apt-get install ros-melodic-joint-state-publisher-gui
```

and then start rviz.launch

```bash
roslaunch my3dbotarm_description rviz.launch
```
