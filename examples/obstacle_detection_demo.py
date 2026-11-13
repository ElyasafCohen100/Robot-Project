from robi.control.robot_controller import RobotController
from robi.sensors.ultrasonic_processor import UltrasonicProcessor

"""Demonstrate obstacle detection and motion decisions."""

# ================================================================= #

def run_demo() -> None:
    """Process an ultrasonic echo and choose a motion command."""
    
    processor = UltrasonicProcessor(window_size = 3)
    controller = RobotController()

    echo_time = 0.002

    distance = processor.process_echo_and_get_median(echo_time)
    command = controller.decide_motion(distance)

    print(f"Distance: {distance:.3f} m")
    print(f"Motion command: {command.value}")
    
# ================================================================= #

