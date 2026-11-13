import pytest
from robi.sensors.ultrasonic_processor import UltrasonicProcessor


# ================================================================================================== #

def test_process_echo_and_get_median_with_single_measurement() -> None:
    """Check that the first echo is converted to distance and returned as the median."""
    
    processor = UltrasonicProcessor(window_size = 3)
    
    echo_time = 0.02
    median_distance = processor.process_echo_and_get_median(echo_time)
    
    assert median_distance == pytest.approx(3.43)
    assert processor.median_filter.measurements == pytest.approx([3.43])
    
# ================================================================================================== #

def test_process_echo_and_get_median_with_multiple_measurements() -> None:
    """Check that multiple echo times are converted to distances and the correct median is returned."""
    
    processor = UltrasonicProcessor(window_size = 3)
    
    speed_of_sound = 343.0
    
    echo_times = [
         2 * 1.0 / speed_of_sound, # 1.0 meters
         2 * 5.0 / speed_of_sound, # 5.0 meters
         2 * 1.2 / speed_of_sound, # 1.2 meters
    ]
    
    for echo_time in echo_times:
        median_distance = processor.process_echo_and_get_median(echo_time)

    assert median_distance == pytest.approx(1.2)
    assert processor.median_filter.measurements == pytest.approx([1.0, 5.0, 1.2])
    
# ================================================================================================== #

def test_process_echo_and_get_median_with_sliding_window() -> None: 
    """Check that the oldest distance is removed and the median is updated."""
    
    processor = UltrasonicProcessor(window_size = 3)
    
    speed_of_sound = 343.0
    
    distances = [1.0, 5.0, 1.2, 4.0] # meters
    echo_times = [2 * distance / speed_of_sound for distance in distances]
    
    for echo_time in echo_times:
        median_distance = processor.process_echo_and_get_median(echo_time)

    assert median_distance == pytest.approx(4.0)
    assert processor.median_filter.measurements == pytest.approx([5.0, 1.2, 4.0])
    
# ================================================================================================== #

def test_process_echo_and_get_median_with_negative_echo_time() -> None:
    """Check that a negative echo time is rejected without updating the filter."""
    
    processor = UltrasonicProcessor(window_size = 3)
    echo_time = -0.02

    with pytest.raises(ValueError):
        processor.process_echo_and_get_median(echo_time)

    assert processor.median_filter.measurements == []
    
# ================================================================================================== #

def test_process_echo_and_get_median_with_negative_echo_time() -> None:
    """Check that a negative echo time does not change existing measurements."""
    
    processor = UltrasonicProcessor(window_size = 3)
    
    # Add a valid measurement first
    processor.median_filter.add_measurement(1.0)
    processor.median_filter.add_measurement(1.2)
    
    echo_time = -0.02
    
    with pytest.raises(ValueError):
        processor.process_echo_and_get_median(echo_time)
    
    assert processor.median_filter.measurements == pytest.approx([1.0, 1.2])
    
# ================================================================================================== #
    
def test_ultrasonic_processors_have_independent_filters() -> None:
    """Check that each processor keeps its own measurements."""
    
    processor_a = UltrasonicProcessor(window_size = 3)
    processor_b = UltrasonicProcessor(window_size = 3)
    
    echo_time = 0.02
    processor_a.process_echo_and_get_median(echo_time)
    
    assert processor_a.median_filter.measurements == pytest.approx([3.43])
    assert processor_b.median_filter.measurements == []
    
# ================================================================================================== #

def test_process_echo_and_get_median_with_zero_echo_time() -> None:
    """Check that zero echo time is accepted and saved as zero distance."""
   
    processor = UltrasonicProcessor(window_size = 3)
    
    echo_time = 0.0
    median_distance = processor.process_echo_and_get_median(echo_time)

    assert median_distance == pytest.approx(0.0)
    assert processor.median_filter.measurements == pytest.approx([0.0])
    
# ================================================================================================== #

    