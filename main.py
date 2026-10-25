"""Run the Project ROBI application."""

import math

from robi.robot import Robot
from robi.odometry import Odometry
from robi.encoders import calculate_wheel_distance

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
 
     odometry.update(
         left_distance = left_distance,
         right_distance = right_distance,
         wheel_separation = wheel_separation
     )
 
     print(odometry.pose)

# ================================================================================== #



if __name__ == "__main__":
    main()
