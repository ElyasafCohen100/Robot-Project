
import pytest
from robi.sensors.median_filter import MedianFilter


# window_size tests:
# =================================================================== #

def test_median_filter_initialization() ->None:
    """Test that a median filter initializes correctly."""
    
    median_filter = MedianFilter(window_size = 3)
    
    assert median_filter.window_size == 3
    assert median_filter.measurements == []

# =================================================================== #

def test_median_filter_zero_window_size() -> None:
    """Test that a zero window size raises ValueError."""

    with pytest.raises(ValueError):
        MedianFilter(window_size = 0)    
    
# =================================================================== #

def test_median_filter_negative_window_size() -> None:
    """Test that a negative window size raises ValueError."""
    
    with pytest.raises(ValueError):
        MedianFilter(window_size = -5)

# =================================================================== #

def test_median_filter_float_window_size() -> None:
    """Test that a floating-point window size raises ValueError."""
   
    with pytest.raises(ValueError):
        MedianFilter(window_size = 2.5)

# =================================================================== #

def test_median_filter_boolean_window_size() -> None:
    """Test that a boolean window size raises ValueError."""
    
    with pytest.raises(ValueError):
        MedianFilter(window_size = True)

# =================================================================== #
