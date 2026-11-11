
from statistics import median


class MedianFilter:
    """Maintain a sliding window of sensor measurements."""
    
# ================================================================================== #

    def __init__(self, window_size: int) -> None:
        """Initialize the median filter with a fixed window size."""
        
        if type(window_size) is not int or window_size <= 0:
             raise ValueError("Window size must be a positive integer.")
        
        self.window_size = window_size
        self.measurements: list[float] = []

# ================================================================================== #

    def add_measurement(self, measurement: float) -> None:
        """Add a new sensor measurement to the filter."""
        
        self.measurements.append(measurement)
        
        if len(self.measurements) > self.window_size:
            self.measurements.pop(0)
        
# ================================================================================== #

    def get_median(self) -> float:
        """Return the median of the current measurements."""
        
        if not self.measurements:
            raise ValueError("No measurements available to calculate median.")
        
        return median(self.measurements)
    
# ================================================================================== #


        
