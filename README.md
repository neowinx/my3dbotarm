# my3dbotarm
ROS Packages for 3DArm+ https://www.thingiverse.com/thing:4023371

# Requirements

- [ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu)
- [Moveit](https://moveit.ros.org/install/)
- [Arduino IDE](https://www.arduino.cc/en/Main/Software) **(in the same host where you've installed ROS)**
- [Git](https://git-scm.com/)

# Installation

```bash
mkdir ~/catkin_ws
cd ~/catkin_ws
git clone https://github.com/neowinx/my3dbotarm.git src
```

# Usage

```bash
roslaunch my3dbotarm_moveit_config demo.launch
```
