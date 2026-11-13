from robi.localization.odometry import Odometry

"""Demonstrate odometry with sensor fusion."""

# ================================================================= #

def run_demo() -> None:
    """Estimate robot pose using encoder and gyroscope data."""
   
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
    
# ================================================================= #

