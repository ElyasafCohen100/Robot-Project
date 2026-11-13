from enum import Enum

class MotionCommand(Enum):
    """Enum representing motion commands for the robot."""
    
    STOP = "stop"
    MOVE_FORWARD = "move_forward"