import rclpy
from rclpy.node import Node
import std_msgs.msg as std_msgs 



class PublishExample(Node):

    def __init__(self) -> None:
        super().__init__('PublishExample')

        self.publisher = self.create_publisher(
            msg_type    = std_msgs.String,
            topic       = 'example_topic',
            qos_profile = 1000
        )

        self.pub_timer = self.create_timer(1., self.pubTimerCallback)

    def pubTimerCallback(self) -> None:
        msg = std_msgs.String()
        msg.data = 'Hello! this is from publisher'
        self.publisher.publish(msg)



def main(args=None) -> None:
    rclpy.init()
    node = PublishExample()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()