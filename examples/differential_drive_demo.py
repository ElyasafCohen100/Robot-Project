import math
from robi.robot import Robot

"""Demonstrate differential-drive robot motion."""

# ================================================================= #

def run_demo() -> None:
    """Simulate a robot driving along a curved path."""
   
    robi = Robot("Robi")

    for step in range(20):
        robi.drive_wheels(
            left_speed = 1.0,
            right_speed = 1.5,
            wheel_separation = 0.5,
            delta_t = 0.1
        )

        print(
            f"Step {step + 1}: "
            f"x={robi.position.x:.2f}, "
            f"y={robi.position.y:.2f}, "
            f"theta={math.degrees(robi.position.theta):.1f}°"
        )
        
# ================================================================= #
