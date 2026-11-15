"""Integration tests for ultrasonic processing and motion decisions."""

from robi.robot_system import RobotSystem
from robi.motion.motion_command import MotionCommand

# ======================================================================================= #

def test_robot_system_stops_when_obstacle_is_close() -> None: 
    """Stop when the processed ultrasonic distance is below the threshold."""

    robot_system = RobotSystem(window_size = 3)
    
    echo_time = 0.002
    command = robot_system.process_echo_and_decide_motion_command(echo_time = echo_time)
    
    assert command == MotionCommand.STOP
    
# ======================================================================================= #

def test_robot_system_uses_median_to_ignore_outlier() -> None:
    """Use the median distance to decide motion despite an outlier."""
    
    robot_system = RobotSystem(window_size = 3)
    
    speed_of_sound = 343.0

    echo_times = [
        2 * 0.3 / speed_of_sound, # 0.3 meters
        2 * 0.4 / speed_of_sound, # 0.4 meters
        2 * 2.0 / speed_of_sound  # 2.0 meters (outlier)
    ]
    
    for echo_time in echo_times:
        command = robot_system.process_echo_and_decide_motion_command(echo_time = echo_time)
        
    assert command == MotionCommand.STOP

# ======================================================================================= #

def test_robot_system_moves_forward_when_obstacle_is_far() -> None:
    """Move forward when the processed distance is above the threshold."""
    
    robot_system = RobotSystem(window_size = 3)

    speed_of_sound = 343.0
    distance = 1.5
  
    echo_time = 2 * distance / speed_of_sound
    command = robot_system .process_echo_and_decide_motion_command(echo_time = echo_time)
    
    assert command == MotionCommand.MOVE_FORWARD
    
# ======================================================================================= #
