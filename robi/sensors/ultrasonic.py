
"""Calculate distances from ultrasonic sensor measurements."""

# ======================================================================================== #

def calculate_distance_from_echo(echo_time: float, speed_of_sound: float = 343.0) -> float:
    """Calculate obstacle distance from the round-trip echo time."""
    
    if echo_time < 0:
        raise ValueError("Echo time must be a positive value.")
    
    if speed_of_sound <= 0:
        raise ValueError("Speed of sound must be a positive value.")
    
    return ( speed_of_sound * echo_time / 2 )

# ======================================================================================== #

def is_obstacle_too_close(distance: float, threshold: float = 0.5) -> bool:
    """Determine if an obstacle is too close based on a distance threshold."""
    
    if distance < 0:
        raise ValueError("Distance must be a positive value.")
    
    if threshold <= 0:
        raise ValueError("Threshold must be a positive value.")
    
    return distance < threshold

# ======================================================================================== #

