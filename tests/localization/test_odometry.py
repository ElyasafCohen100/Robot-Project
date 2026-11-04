"""Test odometry pose estimation from wheel travel distances."""

import math
import pytest

from robi.localization.odometry import Odometry


# encoders's tests #
# ========================================================================================================== #

def test_odometry_straight_motion()->None:
     """Verify that equal wheel distances produce straight motion."""

     odometry = Odometry()
     odometry.update_with_encoders(left_distance = 1.0, right_distance = 1.0, wheel_separation = 0.5)
    
     assert odometry.pose.x == pytest.approx(1.0)
     assert odometry.pose.y == pytest.approx(0.0)
     assert odometry.pose.theta == pytest.approx(0,0)
     
# ========================================================================================================== #

def test_odometry_rotation_in_place()-> None:
    """Verify that opposite wheel distances rotate the robot in place."""
          
    odometry = Odometry()
    odometry.update_with_encoders(left_distance = -0.5, right_distance = 0.5, wheel_separation = 0.5)
    
    assert odometry.pose.x == pytest.approx(0.0)
    assert odometry.pose.y == pytest.approx(0.0)
    assert odometry.pose.theta == pytest.approx(2.0)

# ========================================================================================================== #

def test_odometry_curved_motion() -> None:
    """Verify pose estimation during curved motion."""
   
    odometry = Odometry()
    odometry.update_with_encoders(left_distance = 0.5, right_distance=1.0, wheel_separation=0.5)

    assert odometry.pose.x == pytest.approx(0.75 * math.cos(0.5))
    assert odometry.pose.y == pytest.approx(0.75 * math.sin(0.5))
    assert odometry.pose.theta == pytest.approx(1.0)
        
# ========================================================================================================== #
    
def test_odometry_multiple_updates() -> None:
    """Verify that consecutive updates accumulate robot movement."""
    
    odometry = Odometry()
    odometry.update_with_encoders(left_distance = 1.0, right_distance = 1.0, wheel_separation = 0.5)
    odometry.update_with_encoders(left_distance = 1.0, right_distance = 1.0, wheel_separation = 0.5)

    assert odometry.pose.x == pytest.approx(2.0)
    assert odometry.pose.y == pytest.approx(0.0)
    assert odometry.pose.theta == pytest.approx(0.0)

# ========================================================================================================== #

def test_odometry_rotation_then_forward() -> None:
    """Verify that forward motion uses the heading from a previous update."""

    odometry = Odometry()
    quarter_turn_distance = math.pi / 8
    
    odometry.update_with_encoders(left_distance = -quarter_turn_distance, right_distance = quarter_turn_distance, wheel_separation = 0.5)
    odometry.update_with_encoders(left_distance = 1.0, right_distance = 1.0, wheel_separation = 0.5)

    assert odometry.pose.x == pytest.approx(0.0)
    assert odometry.pose.y == pytest.approx(1.0)

# ========================================================================================================== #



# gyroscope's tests #
# ========================================================================================================== #

def test_odometry_with_gyro_straight_motion() -> None:
    """Verify straight motion using wheel distances and gyroscope data."""
    
    odometry = Odometry()
    odometry.update_with_gyro(left_distance = 1.0, right_distance = 1.0, angular_velocity_z = 0.0, delta_t = 1.0)

    assert odometry.pose.x == pytest.approx(1.0)
    assert odometry.pose.y == pytest.approx(0.0)
    assert odometry.pose.theta == pytest.approx(0.0)
    
# ========================================================================================================== #

def test_odometry_with_gyro_rotation_in_place() -> None: 
    """Verify rotation in place using gyroscope heading change."""
    
    odometry = Odometry()
    odometry.update_with_gyro(left_distance = -0.2, right_distance = 0.2, angular_velocity_z = 0.5, delta_t = 2.0)

    assert odometry.pose.x == pytest.approx(0.0)
    assert odometry.pose.y == pytest.approx(0.0)
    assert odometry.pose.theta == pytest.approx(1.0)
    
# ========================================================================================================== #

def test_odometry_with_gyro_curved_motion() -> None:
    """Verify curved motion using wheel distances and gyroscope data."""
    
    odometry = Odometry()
    odometry.update_with_gyro(left_distance = 0.4, right_distance = 0.6, angular_velocity_z = 1.0, delta_t = 1.0)

    assert odometry.pose.x == pytest.approx(0.5 * math.cos(0.5))
    assert odometry.pose.y == pytest.approx(0.5 * math.sin(0.5))
    assert odometry.pose.theta == pytest.approx(1.0)

# ========================================================================================================== #

def test_odometry_with_gyro_multiple_updates() -> None:
    """Verify pose accumulation across multiple gyroscope-based updates."""
    
    odometry = Odometry()
    
    odometry.update_with_gyro(left_distance = 1.0, right_distance = 1.0, angular_velocity_z = 0.0, delta_t = 1.0)
    odometry.update_with_gyro(left_distance = 0.0, right_distance = 0.0, angular_velocity_z = math.pi / 2, delta_t = 1.0)
    odometry.update_with_gyro(left_distance = 1.0, right_distance = 1.0, angular_velocity_z = 0.0, delta_t = 1.0)

    assert odometry.pose.x == pytest.approx(1.0)
    assert odometry.pose.y == pytest.approx(1.0)
    assert odometry.pose.theta == pytest.approx(math.pi / 2)
    
# ========================================================================================================== #

def test_odometry_with_gyro_negative_delta_t() -> None:
    """Verify that invalid time does not change the estimated pose."""
    
    odometry = Odometry()
    
    odometry.pose.x = 2.0
    odometry.pose.y = 3.0

    with pytest.raises(ValueError):
        odometry.update_with_gyro(left_distance = 1.0, right_distance = 1.0, angular_velocity_z = 0.5, delta_t = -2.0)
        
    assert odometry.pose.x == pytest.approx(2.0)
    assert odometry.pose.y == pytest.approx(3.0)
    assert odometry.pose.theta == pytest.approx(0.0)
    
# ========================================================================================================== #



# sensor_fusion #
# ========================================================================================================== #

def test_odometry_with_sensor_fusion_curved_motion() -> None:
    """Verify that fused sensor data updates the robot's pose."""
    
    odometry = Odometry()
    
    odometry.update_with_sensor_fusion(
        left_distance=0.4,
        right_distance=0.6,
        wheel_separation=0.5,
        angular_velocity_z=0.6,
        delta_t=1.0,
        alpha=0.5
    )

    assert odometry.pose.x == pytest.approx(0.5 * math.cos(0.25))
    assert odometry.pose.y == pytest.approx(0.5 * math.sin(0.25))
    assert odometry.pose.theta == pytest.approx(0.5)

# ========================================================================================================== #

