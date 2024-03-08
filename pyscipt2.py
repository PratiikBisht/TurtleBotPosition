"""Fro this code we can find the specifeic distance of robot from laaser 720 point"""

from robot_control_class import RobotControl

num = int(input("Select a number between 0 and 719: "))

rc = RobotControl()
a = rc.get_laser(num)

print ("The laser value received is: ", a)


"""" the same above program  with little changes like it gets stopped before 1 meter and its logic is in while loop ""

from robot_control_class import RobotControl

robotcontrol = RobotControl()

a = robotcontrol.get_laser(360)

while a > 1:
    robotcontrol.move_straight()
    a = robotcontrol.get_laser(360)
    print ("Current distance to wall: %f" % a)

robotcontrol.stop_robot()

print ("Wall is at %f meters! Stop the robot!" % a)
