from robi.sensors.median_filter import MedianFilter
from robi.sensors.ultrasonic import calculate_distance_from_echo

# ================================================================================================== #

class UltrasonicProcessor:
    """Receive ultrasonic readings, add distances to the median filter, and return the median."""
    
    def __init__(self, window_size: int = 3) -> None:
        """Initialize the processor with a median filter."""
        
        self.median_filter = MedianFilter(window_size = window_size)
        
# ================================================================================================== #

    def process_echo_and_get_median(self, echo_time: float) -> float:
      """Convert echo time to distance, save it in the filter, and return the median."""
      
      distance = calculate_distance_from_echo(echo_time)
      self.median_filter.add_measurement(distance)
      
      return self.median_filter.get_median()
  
# ================================================================================================== #

