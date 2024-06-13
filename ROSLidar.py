import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import time

def callback(data):
    # Convert PointCloud2 message to a list of points
    points = list(pc2.read_points(data, field_names=("x", "y", "z"), skip_nans=True))

    # Process the XYZ data and calculate the time difference for each point
    for i, point in enumerate(points):
        # Get the timestamp of the first point
        start_time = rospy.Time.now().to_sec()
        x, y, z = point
        # Do something with the XYZ data
        print(f"X: {x}, Y: {y}, Z: {z}")

        # Calculate the time difference between the current point and the first point
        current_time = rospy.Time.now().to_sec()
        time_diff = current_time - start_time

        # Print the time difference for each point
        print(f"Time Difference for Point {i+1}: {time_diff:.6f} seconds")

def listener():
    rospy.init_node('lidar_listener', anonymous=True)
    rospy.Subscriber('/lslidar_point_cloud', PointCloud2, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()