"""Estimate a robot's pose from measured wheel travel distances."""

import math

from robi.pose_2d import Pose2D
from robi.imu import calculate_gyro_heading_change
from robi.sensor_fusion import fuse_heading_changes
from robi.geometry import calculate_displacement_midpoint
from robi.differential_drive import(calculate_center_distance, calculate_heading_change)


class Odometry:
    """Track the robot's estimated position and heading."""

# =============================================================================== #

    def __init__(self) -> None:
        """Initialize the robot's estimated pose at the origin."""
        self.pose = Pose2D()
        
# =============================================================================== #
  
    def _update_pose(self, delta_s: float, delta_theta: float) -> None:
        """Update the estimated pose from distance and heading changes."""
        
        delta_x, delta_y = calculate_displacement_midpoint(delta_s, self.pose.theta, delta_theta)
        
        self.pose.x += delta_x
        self.pose.y += delta_y
        self.pose.theta = (self.pose.theta + delta_theta) % math.tau
        
# =============================================================================== #



# ================================================================================================================= #

    def update_with_encoders(self, left_distance: float, right_distance: float, wheel_separation: float) -> None:
        """Update the estimated pose using measured wheel travel distances."""
                        
        delta_s = calculate_center_distance(left_distance, right_distance)
        delta_theta = calculate_heading_change(left_distance, right_distance, wheel_separation)

        self._update_pose(delta_s, delta_theta)    
            
# ================================================================================================================= #

    def update_with_gyro(self, left_distance: float, right_distance: float, angular_velocity_z: float, delta_t: float) -> None:
        """Update the estimated pose using wheel distances and gyroscope data."""

        delta_s = calculate_center_distance(left_distance, right_distance)
        delta_theta = calculate_gyro_heading_change(angular_velocity_z, delta_t)
        
        self._update_pose(delta_s, delta_theta)  
        
# ================================================================================================================= #

    def update_with_sensor_fusion(
        self,
        left_distance: float,
        right_distance: float,
        wheel_separation: float,
        angular_velocity_z: float,
        delta_t: float,
        alpha: float
    ) -> None:
        
        """Update the estimated pose using fused encoder and gyroscope data."""
        
        delta_s = calculate_center_distance(left_distance, right_distance)
        
        encoder_delta_theta = calculate_heading_change(left_distance, right_distance, wheel_separation)
        gyro_delta_theta = calculate_gyro_heading_change(angular_velocity_z, delta_t)
        
        fused_delta_theta = fuse_heading_changes(encoder_delta_theta, gyro_delta_theta, alpha)
        self._update_pose(delta_s, fused_delta_theta) 
        
# ================================================================================================================= #
