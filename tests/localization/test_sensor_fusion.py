"""Test sensor fusion calculations for robot heading changes."""

import math
import pytest

from robi.localization.odometry import Odometry
from robi.localization.sensor_fusion import fuse_heading_changes

# ============================================================================================ #

def test_fuse_heading_changes_weighted_average() -> None:
    """Verify weighted averaging of encoder and gyroscope heading changes."""
    
    result = fuse_heading_changes(encoder_delta_theta = 0.4, gyro_delta_theta = 0.6, alpha = 0.7)
    assert result == pytest.approx(0.54)
    
# ============================================================================================ #

def test_fuse_heading_changes_encoder_only() -> None:
    """Verify that zero gyro weight uses only the encoder measurement."""
    
    result = fuse_heading_changes(encoder_delta_theta = 0.4, gyro_delta_theta = 0.6, alpha = 0.0)
    assert result == pytest.approx(0.4)

# ============================================================================================ #

def test_fuse_heading_changes_gyro_only() -> None:
    """Verify that full gyro weight uses only the gyroscope measurement."""
    
    result = fuse_heading_changes(encoder_delta_theta = 0.4, gyro_delta_theta = 0.6, alpha = 1.0)
    assert result == pytest.approx(0.6)

# ============================================================================================ #

def test_fuse_heading_changes_negative_alpha() -> None:
    """Verify that a negative sensor weight raises ValueError."""
    
    with pytest.raises(ValueError):
        fuse_heading_changes(encoder_delta_theta = 0.4, gyro_delta_theta = 0.6, alpha = -0.2)
        
# ============================================================================================ #

def test_fuse_heading_changes_alpha_above_one() -> None:
    """Verify that a sensor weight above one raises ValueError."""
    
    with pytest.raises(ValueError):
        fuse_heading_changes(encoder_delta_theta = 0.4, gyro_delta_theta = 0.6, alpha = 1.5)
        
# ============================================================================================ #

def test_odometry_with_sensor_fusion_multiple_updates() -> None:
    """Verify that fused odometry accumulates motion across updates."""
    
    odometry = Odometry()

    odometry.update_with_sensor_fusion(
        left_distance = 1.0,
        right_distance = 1.0,
        wheel_separation = 0.5,
        angular_velocity_z = 0.0,
        delta_t = 1.0,
        alpha = 0.5
    )

    odometry.update_with_sensor_fusion(
        left_distance = -math.pi / 8,
        right_distance = math.pi / 8,
        wheel_separation = 0.5,
        angular_velocity_z = math.pi / 2,
        delta_t = 1.0,
        alpha = 0.5
    )

    odometry.update_with_sensor_fusion(
        left_distance = 1.0,
        right_distance = 1.0,
        wheel_separation = 0.5,
        angular_velocity_z = 0.0,
        delta_t = 1.0,
        alpha = 0.5
    )

    assert odometry.pose.x == pytest.approx(1.0)
    assert odometry.pose.y == pytest.approx(1.0)
    assert odometry.pose.theta == pytest.approx(math.pi / 2)

# ============================================================================================ #

def test_odometry_with_sensor_fusion_invalid_alpha() -> None:
    """Verify that invalid sensor weight does not change the pose."""
   
    odometry = Odometry()

    odometry.pose.x = 2.0
    odometry.pose.y = 3.0
    odometry.pose.theta = 0.5

    with pytest.raises(ValueError):
        odometry.update_with_sensor_fusion(
            left_distance = 0.4,
            right_distance = 0.6,
            wheel_separation = 0.5,
            angular_velocity_z = 0.6,
            delta_t = 1.0,
            alpha = 1.5
        )

    assert odometry.pose.x == pytest.approx(2.0)
    assert odometry.pose.y == pytest.approx(3.0)
    assert odometry.pose.theta == pytest.approx(0.5)
    
# ============================================================================================ #

