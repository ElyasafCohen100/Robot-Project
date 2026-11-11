from robi.sensors.median_filter import MedianFilter

class UltrasonicProcessor:
    """Coordinate ultrasonic measurements and median filtering."""
    
    def __init__(self, window_size: int = 3) -> None:
        """Initialize the processor with a median filter."""
        
        self.median_filter = MedianFilter(window_size = window_size)
        
        