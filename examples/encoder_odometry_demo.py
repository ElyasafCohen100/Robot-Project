from robi.localization.odometry import Odometry
from robi.sensors.encoders import calculate_wheel_distance

"""Demonstrate odometry using wheel encoders."""

# ================================================================= #

def run_demo() -> None:
    """Estimate robot motion from encoder pulses."""
    
    odometry = Odometry()

    left_pulses = 100
    right_pulses = 100

    wheel_diameter = 0.1
    wheel_separation = 0.5
    pulses_per_revolution = 100

    left_distance = calculate_wheel_distance(
        pulses=left_pulses,
        pulses_per_revolution=pulses_per_revolution,
        wheel_diameter=wheel_diameter
    )

    right_distance = calculate_wheel_distance(
        pulses=right_pulses,
        pulses_per_revolution=pulses_per_revolution,
        wheel_diameter=wheel_diameter
    )

    odometry.update_with_encoders(
        left_distance=left_distance,
        right_distance=right_distance,
        wheel_separation=wheel_separation
    )

    print("Encoder Odometry Pose:", odometry.pose)
    
# ================================================================= #
