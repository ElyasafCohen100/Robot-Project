"""Provide calculations for inertial sensor measurements."""

# ================================================================================== #

def calculate_gyro_heading_change(angular_velocity_z: float, delta_t: float) -> float:
    """Calculate heading change from gyroscope angular velocity."""
    
    if delta_t < 0:
        raise ValueError("Time step cannot be negative")

    return angular_velocity_z * delta_t

# ================================================================================== #
