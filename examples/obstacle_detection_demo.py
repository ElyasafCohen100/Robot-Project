"""Demonstrate obstacle detection and motion decisions."""

from robi.robot_system import RobotSystem


# ======================================================================================== #

def run_demo() -> None:
    """Process an ultrasonic echo and choose a motion command."""
    
    robot_system = RobotSystem(window_size = 3)
    
    echo_time = 0.002
    command = robot_system.process_echo_and_decide_motion_command(echo_time = echo_time)

    print(f"Motion command: {command.value}")
    
# ======================================================================================== #
