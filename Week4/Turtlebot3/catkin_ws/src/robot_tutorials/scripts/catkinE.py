import rospy
from std_msgs.msg import String


def catkinE_talker():
    hello_pub = rospy.Publisher('hello', String, queue_size=10)
    rospy.init_node('catkinE', anonymous=False)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        greeting = "Hello, Shahd!"
        rospy.loginfo(greeting)
        hello_pub.publish(greeting)
        rate.sleep()

if __name__ == '__main__':
    try:
        catkinE_talker()
    except rospy.ROSInterruptException:
        pass



