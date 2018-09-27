#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import serial
from geometry_msgs.msg import PoseStamped
import json

ser = serial.Serial('/dev/ttyUSB1', 9600)
data = []
right_dim = 280
delta = 10

def talker():
 count = 0
 while not rospy.is_shutdown():
   
   char= ser.read()
   data.append(char)
   
   
   if ((right_dim - delta < len(data) < right_dim + delta) and char == '!'): #EOM
	     
       pose_str = ''.join(data) 
       #print "\n lungh data" + str(len(data))
       del data[:]
       pose_c = pose_str.decode('utf8').replace("\n", '').replace("!", '').split('position:')

       if len(pose_c) > 1:
           pose = pose_c[1].split('orientation:')
           if len(pose) > 1:

               pose_position = "{" + pose[0].replace("x:" , '\"x\" : \"').replace("y:", ' \" , \"y\" : \"').replace("z:", '\" , \"z\" : \"') + "\"}"
               pose_orientation = "{" + pose[1].replace("x:", '\"x\" : \"').replace("y:", ' \" , \"y\" : \"').replace("z:", '\" , \"z\" : \"').replace("w:", '\" , \"w\" : \"') + "\"}"

               try:               
                 p_position_j = json.loads(pose_position)
                 p_orientation_j = json.loads(pose_orientation)


                 pose_msg = PoseStamped()
                 pose_msg.pose.position.x = float(p_position_j["x"])
                 pose_msg.pose.position.y = float(p_position_j["y"])
                 pose_msg.pose.position.z = float(p_position_j["z"])

                 pose_msg.pose.orientation.x = float(p_orientation_j["x"])
                 pose_msg.pose.orientation.y = float(p_orientation_j["y"])
                 pose_msg.pose.orientation.z = float(p_orientation_j["z"])
                 pose_msg.pose.orientation.w = float(p_orientation_j["w"])
                 pass
               except Exception as e:
                 print "Oops!  That was no valid number.  Try again..."
               

               pub.publish(pose_msg)
               print pose_msg
   elif (right_dim - delta < len(data) and char == '!'):
       print " bad value, delete because too long package  " + str(len(data))
       del data[:] 
   
if __name__ == '__main__':
  try:
    print 'start serial comm..'
    
    pub = rospy.Publisher('pose_xbee', PoseStamped, queue_size=1)
    rospy.init_node('ros_receiver')
    talker()
  except rospy.ROSInterruptException:
    pass
