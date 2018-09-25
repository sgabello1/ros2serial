#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import serial
from geometry_msgs.msg import PoseStamped

ser = serial.Serial('/dev/ttyUSB0', 9600)


def talker():
 while not rospy.is_shutdown():
   
   data= ser.read(50) # I have "hi" coming from the arduino as a test run over the serial port
   rospy.loginfo(data)
   pub.publish(PoseStamped(data))
   #rospy.sleep(1.0)

if __name__ == '__main__':
  try:
    print 'start serial comm..'
    pub = rospy.Publisher('pose', PoseStamped, queue_size=10)
    rospy.init_node('ros_receiver')
    talker()
  except rospy.ROSInterruptException:
    pass