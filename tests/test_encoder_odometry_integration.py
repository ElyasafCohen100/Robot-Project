
"""Test integration between wheel encoders and odometry."""

import math
import pytest

# integration test (encoders & odometry) #
from robi.odometry import Odometry
from robi.encoders import calculate_wheel_distance

# ============================================================================================ #

def test_encoder_odometry_straight_motion() -> None:
    """Verify that encoder pulses produce correct straight-line odometry."""
   
    odometry = Odometry()

    left_distance = calculate_wheel_distance(
        pulses = 100,
        pulses_per_revolution = 100,
        wheel_diameter = 0.1
    )

    right_distance = calculate_wheel_distance(
        pulses = 100,
        pulses_per_revolution = 100,
        wheel_diameter = 0.1
    )

    odometry.update_with_encoders(
        left_distance = left_distance,
        right_distance = right_distance,
        wheel_separation = 0.5
    )

    assert odometry.pose.x == pytest.approx(math.pi * 0.1)
    assert odometry.pose.y == pytest.approx(0.0)
    assert odometry.pose.theta == pytest.approx(0.0)

# ============================================================================================ #

def test_encoder_gyro_odometry_integration() -> None:
    """Verify integration of encoder distances and gyroscope heading."""
    
    odometry = Odometry()

    left_distance = calculate_wheel_distance(
        pulses = 100,
        pulses_per_revolution = 100,
        wheel_diameter = 0.1
    )

    right_distance = calculate_wheel_distance(
        pulses = 100,
        pulses_per_revolution = 100,
        wheel_diameter = 0.1
    )

    odometry.update_with_gyro(
        left_distance = left_distance,
        right_distance = right_distance,
        angular_velocity_z = 1.0,
        delta_t = 1.0
    )

    center_distance = math.pi * 0.1
    
    assert odometry.pose.x == pytest.approx(center_distance * math.cos(0.5))
    assert odometry.pose.y == pytest.approx(center_distance * math.sin(0.5))
    assert odometry.pose.theta == pytest.approx(1.0)

# ============================================================================================ #
