#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    ser.write(str(data))
    ser.close()
    
def listener():

    rospy.init_node('broadcaster', anonymous=True)

    rospy.Subscriber("/fake_pose", PoseStamped, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()