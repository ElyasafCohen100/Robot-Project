"""Combine sensor measurements for robot navigation."""

# ============================================================================================ #

def fuse_heading_changes(encoder_delta_theta: float, gyro_delta_theta: float, alpha: float) -> float:
    """Combine encoder and gyroscope heading changes using weighted averaging."""
     
    if not 0.0 <= alpha <= 1:
        raise ValueError("Alpha must be between 0 and 1")
     
    return (alpha * gyro_delta_theta + (1 - alpha) * encoder_delta_theta)

# ============================================================================================ #

