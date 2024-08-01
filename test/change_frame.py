# change_frame.py
import rosbag
from std_msgs.msg import Header

input_bag_path = 'test1.bag'  # Path to your input rosbag file
output_bag_path = 'test1_fix.bag'  # Path to the modified rosbag file

def modify_header(msg):
    """Modify the frame_id in the header of the message."""
    if hasattr(msg, 'header'):
        if msg.header.frame_id == '/gps':
            msg.header.frame_id = 'gps_link'
    return msg

with rosbag.Bag(input_bag_path, 'r') as in_bag, rosbag.Bag(output_bag_path, 'w') as out_bag:
    for topic, msg, t in in_bag.read_messages():
        msg = modify_header(msg)
        out_bag.write(topic, msg, t)

print("Processed bag file saved to: {output_bag_path}")
