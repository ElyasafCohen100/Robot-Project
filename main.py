"""Run the Project ROBI application."""

import math

from robi.robot import Robot
from robi.localization.odometry import Odometry
from robi.sensors.encoders import calculate_wheel_distance

# ================================================================================== #

def main() -> None:
     """Simulate a robot driving along a curved path."""
     
     robi = Robot("Robi")
     
     for step in range(20):
         
        robi.drive_wheels(       
               left_speed=1.0,
               right_speed=1.5,
               wheel_separation=0.5,
               delta_t=0.1
           )
         
        print(
            f"Step {step + 1}: "
            f"x={robi.position.x:.2f}, "
            f"y={robi.position.y:.2f}, "
            f"theta={math.degrees(robi.position.theta):.1f}°"
        )

# ================================================================================== #

     odometry = Odometry()
 
     left_pulses = 100
     right_pulses = 100
     
     wheel_diameter = 0.1
     wheel_separation = 0.5
     
     pulses_per_revolution = 100
 
 
     left_distance = calculate_wheel_distance(
         pulses = left_pulses,
         pulses_per_revolution = pulses_per_revolution,
         wheel_diameter = wheel_diameter
     )
 
     right_distance = calculate_wheel_distance(
         pulses = right_pulses,
         pulses_per_revolution = pulses_per_revolution,
         wheel_diameter = wheel_diameter
     )
 
     odometry.update_with_encoders(
         left_distance = left_distance,
         right_distance = right_distance,
         wheel_separation = wheel_separation
     )
 
     print(odometry.pose)

# ================================================================================== #

# Sensor fusion demonstration
fusion_odometry = Odometry()

fusion_odometry.update_with_sensor_fusion(
    left_distance = 0.4,
    right_distance = 0.6,
    wheel_separation = 0.5,
    angular_velocity_z = 0.6,
    delta_t = 1.0,
    alpha = 0.8
)

print("Sensor Fusion Pose:", fusion_odometry.pose)

# ================================================================================== #



if __name__ == "__main__":
    main()
