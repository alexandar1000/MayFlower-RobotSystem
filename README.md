# MayFlower-RobotSystem

## Sensor Messages
**Planar Laser Messages**

`sensor_msgs/LaserScan` or `sensor_msgs/PointCloud2`

To inspect the message format, use:

`rosmsg show sensor_msgs/LaserScan`

Format:

```bash
std_msgs/Header header 
  uint32 seq 
  time stamp 
  string frame_id 
float32 angle_min 
float32 angle_max 
float32 angle_increment 
float32 time_increment 
float32 scan_time 
float32 range_min 
float32 range_max 
float32[] ranges 
float32[] intensities 
```



##### LaserScanners Characteristics

* Minimum Angle
* Maximum Angle
* Angle Measurement
* Time Increment
* Scan Time
* Minimum Range
* Maximum Range
* List of Ranges
* List of Intensities