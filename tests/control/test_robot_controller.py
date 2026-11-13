from robi.motion.motion_command import MotionCommand
from robi.control.robot_controller import RobotController

# ================================================================================== #

def test_decide_motion_stops_when_obstacle_is_too_close() -> None:
    """Check that the robot stops when an obstacle is too close."""
    
    controller = RobotController()
    command = controller.decide_motion(distance = 0.2)
   
    assert command == MotionCommand.STOP
    
# ================================================================================== #

def test_decide_motion_moves_forward_when_obstacle_is_far() -> None:
    """Check that the robot moves forward when an obstacle is far enough."""
   
    controller = RobotController()
    command = controller.decide_motion(distance = 1.5)

    assert command == MotionCommand.MOVE_FORWARD

# ================================================================================== #

def test_decide_motion_moves_forward_at_stop_threshold() -> None:
    """Check that the robot moves forward when distance equals the stop threshold."""
    
    controller = RobotController()
    command = controller.decide_motion(distance = 0.5)

    assert command == MotionCommand.MOVE_FORWARD
    
# ================================================================================== #

