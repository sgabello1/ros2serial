## XBee ROS to Serial

In this package there are two nodes: ros_broadcast.py and ros_receiver.py. 

**ros_broadcast.py** subscribes to ROS PoseStamped message coming out the topic */vrpn_client_node/husky/pose* and streams it into serial port /dev/ttyUSB0.

Launch it in the machine where you have VRPN client in ROS.

rosrun ros2serial ros_broadcast.py


**ros_receive.py** read data coming from the serial port /dev/ttyUSB0 and process it in a ROS message PoseStamped. 

LIMITATION:

This code is not implemented with Python XBee APIs, it's the raw direct serial communication. 
It's implemented a brute force (hardcoded) way to understand if the package is correct according to the lenght of the package.

rosrun ros2serial ros_receiver.py


Packages needed:
- pyserial
- rospy
- json
