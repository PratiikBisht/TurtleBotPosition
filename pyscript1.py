cd ~/catkin_ws/src/
mkdir robot_control
cd robot_control

from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser(360)

print ("The distance measured is: ", a, " m.")
