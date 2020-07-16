import rospy
from std_msgs.msg import String
def callback_str(data):
    rospy.loginfo(data.data)
def Shahd_listener():
    rospy.init_node('Shahd', anonymous=False)
    rospy.Subscriber('hello', String, callback_str)
    rospy.spin()

if __name__ == '__main__':
    Shahd_listener()

