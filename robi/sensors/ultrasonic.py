
"""Calculate distances from ultrasonic sensor measurements."""

# ======================================================================================== #

def calculate_distance_from_echo(echo_time: float, speed_of_sound: float = 343.0) -> float:
    """Calculate obstacle distance from the round-trip echo time."""
    
    if echo_time <= 0:
        raise ValueError("Echo time must be a positive value.")
    
    if speed_of_sound < 0:
        raise ValueError("Speed of sound must be a positive value.")
    
    return ( speed_of_sound * echo_time / 2 )

# ======================================================================================== #


 