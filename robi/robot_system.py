from robi.motion.motion_command import MotionCommand
from robi.control.robot_controller import RobotController
from robi.sensors.ultrasonic_processor import UltrasonicProcessor

"""Coordinate robot sensors and motion decisions."""

# ================================================================================== #

class RobotSystem:
    """Coordinate sensor processing and motion decisions."""
    
    def __init__(self, window_size: int = 3) -> None:
        self.ultrasonic_processor = UltrasonicProcessor(window_size = window_size)
        self.robot_controller = RobotController()
        
# ================================================================================== #

    def process_echo_and_decide_motion_command(self, echo_time: float) -> MotionCommand:
        """Process an ultrasonic echo and return a motion command."""
        
        distance = self.ultrasonic_processor.process_echo_and_get_median(echo_time)
        return self.robot_controller.decide_motion(distance)

# ================================================================================== #
