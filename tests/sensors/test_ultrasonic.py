"""Tests for ultrasonic distance calculations."""

import pytest
from robi.sensors.ultrasonic import calculate_distance_from_echo, is_obstacle_too_close



# distance = (speed_of_sound * echo_time / 2)
# ================================================================================== #

def test_calculate_distance_from_echo() -> None:
    """Test distance calculation for a valid echo time."""
    
    echo_time = 0.02 # seconds
    distance = calculate_distance_from_echo(echo_time)
    
    assert distance == pytest.approx(3.43)
    
# ================================================================================== #

def test_negative_echo_time() -> None:
    """Test that a negative echo time raises a ValueError."""
    
    echo_time = -0.02 # seconds
    
    with pytest.raises(ValueError):
        calculate_distance_from_echo(echo_time) 
        
# ================================================================================== #

def test_negative_speed_of_sound() -> None:
    """Test that negative speed of sound raises ValueError."""

    with pytest.raises(ValueError):
        calculate_distance_from_echo(echo_time = 0.02, speed_of_sound = -343.0)

# ================================================================================== #

def test_zero_speed_of_sound() -> None:
    """Test that zero speed of sound raises ValueError."""

    with pytest.raises(ValueError):
        calculate_distance_from_echo(echo_time = 0.02, speed_of_sound = 0.0)

# ================================================================================== #

def test_zero_echo_time() -> None:
    """Test that zero echo time returns zero distance."""
    
    echo_time = 0.0
    distance = calculate_distance_from_echo(echo_time)
    
    assert distance == pytest.approx(0.0)
    
# ================================================================================== #

def  test_custom_speed_of_sound() -> None:
    """Test distance calculation with a custom speed of sound."""
    
    distance = calculate_distance_from_echo(echo_time = 0.02, speed_of_sound = 340.0)
    assert distance == pytest.approx(3.4)   
    
# ================================================================================== #



# is_obstacle_too_close
# ================================================================================== #

def test_is_obstacle_too_close() -> None:
    """Test that an obstacle below the threshold is too close."""
    
    result = is_obstacle_too_close(distance = 0.3, threshold = 0.5)
    assert result is True

# ================================================================================== #

def test_obstacle_not_too_close() -> None:
    """Test that a distant obstacle is not too close."""

    result = is_obstacle_too_close(distance = 1.0, threshold = 0.5)
    assert result is False
    
# ================================================================================== #

def test_obstacle_at_threshold() -> None:
    """Test that an obstacle exactly at the threshold is not too close."""

    result = is_obstacle_too_close(distance = 0.5, threshold = 0.5)
    assert result is False
    
# ================================================================================== #

def test_obstacle_negative_distance() -> None:
    """Test that negative obstacle distance raises ValueError."""
    
    with pytest.raises(ValueError):
        is_obstacle_too_close(distance = -2.0, threshold = 0.5)
        
# ================================================================================== #

def test_obstacle_zero_threshold() -> None:
    """Test that a zero safety threshold raises ValueError."""
    
    with pytest.raises(ValueError):
        is_obstacle_too_close(distance = 0.3, threshold = 0.0)  

# ================================================================================== #

def test_obstacle_default_threshold() -> None:
    """Test obstacle detection using the default safety threshold."""

    result = is_obstacle_too_close(distance = 0.3)# Using default threshold of 0.5
    assert result is True

# ================================================================================== #
