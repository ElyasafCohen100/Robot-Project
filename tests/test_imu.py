"""Test gyroscope-based heading calculations."""

import pytest
from robi.imu import calculate_gyro_heading_change


# angular velocity #
# ====================================================================================== #

def test_gyro_positive_angular_velocity() -> None:
    """Verify heading change for positive angular velocity."""
    
    delta_theta = calculate_gyro_heading_change(angular_velocity_z = 0.5, delta_t = 2.0)
    assert delta_theta == pytest.approx(1.0) 

# ====================================================================================== #

def test_gyro_negative_angular_velocity() -> None:
    """Verify heading change for negative angular velocity."""

    delta_theta = calculate_gyro_heading_change(angular_velocity_z = -0.5, delta_t = 2.0)
    assert delta_theta == pytest.approx(-1.0)
    
# ====================================================================================== #

def test_gyro_zero_angular_velocity() -> None:
    """Verify zero heading change when angular velocity is zero."""
    
    delta_theta = calculate_gyro_heading_change(angular_velocity_z = 0.0, delta_t = 5.0)
    assert delta_theta == pytest.approx(0.0)
    
# ====================================================================================== #



# delta theta #
# ====================================================================================== #

def test_gyro_zero_delta_t() -> None:
    """Verify zero heading change when the time step is zero."""
    
    delta_theta = calculate_gyro_heading_change(angular_velocity_z = 1.5, delta_t = 0.0)
    assert delta_theta == pytest.approx(0.0)
    
# ====================================================================================== #

def test_gyro_negative_delta_t() -> None:
    """Verify that a negative time step raises a ValueError."""

    with pytest.raises(ValueError):
        calculate_gyro_heading_change(angular_velocity_z = 0.5, delta_t = -2.0)

# ====================================================================================== #

