

class MedianFilter:
    """Maintain a sliding window of sensor measurements."""
    
# ================================================================================== #

    def __init__(self, window_size:int) -> None:
        """Initialize the median filter with a fixed window size."""
        
        if type(window_size) is not int or window_size <= 0:
             raise ValueError("Window size must be a positive integer.")
        
        self.window_size = window_size
        self.measurements: list[float] = []

# ================================================================================== #

