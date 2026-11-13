from robi.motion.motion_command import MotionCommand
from robi.sensors.ultrasonic import is_obstacle_too_close

class RobotController:
    """Choose robot motion commands based on sensor information."""

# ================================================================================== #

    def decide_motion(self, distance: float) -> MotionCommand:
         """Choose a motion command based on obstacle distance."""

         if is_obstacle_too_close(distance):
             return MotionCommand.STOP  


         return MotionCommand.MOVE_FORWARD
# ================================================================================== #
