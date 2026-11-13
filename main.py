from examples.sensor_fusion_demo import run_demo as run_sensor_fusion
from examples.encoder_odometry_demo import run_demo as run_encoder_odometry
from examples.obstacle_detection_demo import run_demo as run_obstacle_detection
from examples.differential_drive_demo import run_demo as run_differential_drive

"""Run the Project ROBI application."""


def main() -> None:
    """Run the selected Project ROBI demonstration."""

    demos = {
        "1": run_differential_drive,
        "2": run_encoder_odometry,
        "3": run_sensor_fusion,
        "4": run_obstacle_detection
    }

    print("======= Project ROBI =======")
    print("1. Differential Drive")
    print("2. Encoder Odometry")
    print("3. Sensor Fusion")
    print("4. Obstacle Detection")

    choice = input("Choose a demo (1-4): ")

    selected_demo = demos.get(choice)

    if selected_demo is None:
        print("Invalid selection.")
        return

    selected_demo()


if __name__ == "__main__":
    main()