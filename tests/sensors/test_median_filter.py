
import pytest
from robi.sensors.median_filter import MedianFilter


# window_size tests:
# ================================================================================ #

def test_median_filter_initialization() ->None:
    """Test that a median filter initializes correctly."""
    
    median_filter = MedianFilter(window_size = 3)
    
    assert median_filter.window_size == 3
    assert median_filter.measurements == []

# ================================================================================ #

def test_median_filter_zero_window_size() -> None:
    """Test that a zero window size raises ValueError."""

    with pytest.raises(ValueError):
        MedianFilter(window_size = 0)    
    
# ================================================================================ #

def test_median_filter_negative_window_size() -> None:
    """Test that a negative window size raises ValueError."""
    
    with pytest.raises(ValueError):
        MedianFilter(window_size = -5)

# ================================================================================ #

def test_median_filter_float_window_size() -> None:
    """Test that a floating-point window size raises ValueError."""
   
    with pytest.raises(ValueError):
        MedianFilter(window_size = 2.5)

# ================================================================================ #

def test_median_filter_boolean_window_size() -> None:
    """Test that a boolean window size raises ValueError."""
    
    with pytest.raises(ValueError):
        MedianFilter(window_size = True)

# ================================================================================ #



# list measurements tests:
# ================================================================================ #

def test_median_filter_add_measurement() -> None:
    """Test that a new measurement is added to the filter."""
    
    median_filter = MedianFilter(window_size = 3)
    median_filter.add_measurement(1.5)
    
    assert median_filter.measurements == [1.5]
    
# ================================================================================ #

def test_median_filter_add_multiple_measurements() -> None:
    """Test that multiple measurements are stored in order."""
   
    median_filter = MedianFilter(window_size = 3)

    median_filter.add_measurement(1.0)
    median_filter.add_measurement(1.2)
    median_filter.add_measurement(0.9)

    assert median_filter.measurements == [1.0, 1.2, 0.9]

# ================================================================================ #

def test_median_filter_removes_oldest_measurement() -> None:
    """Test that the oldest measurement is removed when the window is full."""
   
    median_filter = MedianFilter(window_size = 3)

    median_filter.add_measurement(1.0)
    median_filter.add_measurement(1.2)
    median_filter.add_measurement(0.9)
    median_filter.add_measurement(5.0)

    assert median_filter.measurements == [1.2, 0.9, 5.0]
    
# ================================================================================ #

def test_median_filter_window_size_one() -> None:
    """Test that a window of size one keeps only the latest measurement."""
   
    median_filter = MedianFilter(window_size = 1)

    median_filter.add_measurement(2.0)
    median_filter.add_measurement(3.5)
    median_filter.add_measurement(1.2)

    assert median_filter.measurements == [1.2]

# ================================================================================ #

def test_median_filter_keeps_latest_measurements() -> None:
    """Test that the filter keeps only the latest measurements over time."""
   
    median_filter = MedianFilter(window_size = 3)

    for measurement in [1.0, 1.1, 0.9, 5.0, 1.2, 1.3]:
        median_filter.add_measurement(measurement)

    assert median_filter.measurements == [5.0, 1.2, 1.3] 

# ================================================================================ #



#calculates median tests:
# ================================================================================ # 

def test_median_filter_calculates_median() -> None:
    """Test that the filter calculates the median of three measurements."""
    
    median_filter = MedianFilter(window_size = 3)

    median_filter.add_measurement(1.0)
    median_filter.add_measurement(8.0)
    median_filter.add_measurement(1.2)

    assert median_filter.get_median() == pytest.approx(1.2)
    
# ================================================================================ # 

def test_median_filter_calculates_median_with_even_measurements() -> None:
    """Test that the median is averaged for an even number of measurements."""
  
    median_filter = MedianFilter(window_size = 4)

    median_filter.add_measurement(1.0)
    median_filter.add_measurement(8.0)
    median_filter.add_measurement(1.2)
    median_filter.add_measurement(1.4)

    assert median_filter.get_median() == pytest.approx(1.3)

# ================================================================================ # 

def test_median_filter_get_median_with_no_measurements() -> None:
    """Test that calculating the median without measurements raises ValueError."""
    
    median_filter = MedianFilter(window_size = 3)
    
    with pytest.raises(ValueError, match = "No measurements available to calculate median."):
        median_filter.get_median()
        
# ================================================================================ # 

def test_median_filter_calculates_median_before_window_is_full() -> None:
    """Test that the median is available before the window fills."""
   
    median_filter = MedianFilter(window_size = 5)

    median_filter.add_measurement(2.0)
    median_filter.add_measurement(4.0)

    assert median_filter.get_median() == pytest.approx(3.0)
    
# ================================================================================ # 

def test_median_filter_calculates_median_after_window_slides() -> None:
    """Test that the median uses only measurements in the current window."""
   
    median_filter = MedianFilter(window_size = 3)

    for measurement in [1.0, 1.2, 0.9, 5.0, 1.1]:
        median_filter.add_measurement(measurement)  

    assert median_filter.measurements == [0.9, 5.0, 1.1]
    assert median_filter.get_median() == pytest.approx(1.1)
    
# ================================================================================ # 

