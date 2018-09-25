#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import serial
from geometry_msgs.msg import PoseStamped

ser = serial.Serial('/dev/ttyUSB0', 9600)
data = []



def talker():
 count = 0
 while not rospy.is_shutdown():
   
   char= ser.read()
   data.append(char)
   
   if char == 'w' or count > 0:
	count += 1

   if  count > 5: # EOM
       count = 0
       pose_str = ''.join(data)
       del data[:]
       rospy.loginfo(pose_str)
       pub.publish(String(pose_str))
   
if __name__ == '__main__':
  try:
    print 'start serial comm..'
    
    pub = rospy.Publisher('pose', String, queue_size=1)
    rospy.init_node('ros_receiver')
    talker()
  except rospy.ROSInterruptException:
    pass
