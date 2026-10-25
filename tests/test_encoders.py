"""Test wheel encoder distance calculations."""

import math
import pytest

from robi.encoders import calculate_wheel_distance

# ================================================================================== #

def test_encoder_one_full_rotation()-> None:
    """Verify the distance traveled in one full wheel rotation."""
    
    distance = calculate_wheel_distance(pulses = 100, pulses_per_revolution = 100, wheel_diameter = 0.1)
    assert distance == pytest.approx(math.pi * 0.1)

# ================================================================================== #

def test_encoder_backward_rotation()-> None:
    """Verify that negative pulses produce negative travel distance."""
    
    distance = calculate_wheel_distance(pulses = -100, pulses_per_revolution = 100, wheel_diameter = 0.1)
    assert distance == pytest.approx(-math.pi * 0.1)
    
# ================================================================================== #

def test_encoder_zero_pulses() -> None:
    """Verify that zero pulses produce zero travel distance."""
    
    distance = calculate_wheel_distance(pulses = 0, pulses_per_revolution = 100, wheel_diameter = 0.1)
    assert distance == pytest.approx(0.0)
    
# ================================================================================== #

def test_encoder_zero_ppr() -> None:
    """Verify that zero pulses per revolution raises ValueError."""
    with pytest.raises(ValueError):
        calculate_wheel_distance(pulses = 100, pulses_per_revolution = 0, wheel_diameter = 0.1 )

# ================================================================================== #

def test_encoder_invalid_wheel_diameter() -> None:
    """Verify that non-positive wheel diameter raises ValueError."""
    with pytest.raises(ValueError):
        calculate_wheel_distance(pulses = 100, pulses_per_revolution = 100, wheel_diameter = -0.1)
        
# ================================================================================== #