#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
import serial


def callback(data):
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    
    if ser.isOpen():
        ser.write(str(data) + "!") # ! is my EOM
        ser.close()
    
def listener():

    rospy.init_node('broadcaster', anonymous=True)

    rospy.Subscriber("/vrpn_client_node/husky/pose", PoseStamped, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()