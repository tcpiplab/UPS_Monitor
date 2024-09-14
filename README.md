# UPS Monitor

This Python script monitors the power status of a computer and alerts the user when a power outage is detected and the system is running on battery power. It provides an audible alert (using text-to-speech on macOS) with the remaining battery time and percentage.

## Features

- Checks the battery status periodically (every 60 seconds by default)
- Alerts the user with an audible message when the system is running on battery power
- Displays the remaining battery time and percentage in the alert message
- Respects a configurable time range for audible alerts (e.g., only during working hours)

## Requirements

- Python 3.x
- `psutil` library (install with `pip install psutil`)
- A computer running MacOS
- An APC UPS battery
- A USB cable running between the Mac and the UPS

## Usage

1. Clone the repository or download the `ups_monitor.py` file.
2. Install the required dependency: `pip install psutil`.
3. Run the script: `python ups_monitor.py`
4. **Optional**: Call the script from your crontab at `@reboot` so that it is always running.
5. **Optional**: Set up a virtual environment to make sure that the Python runtime called by crontab can find the `psutil` library.

The script will run continuously, checking the power status every 60 seconds. When a power outage is detected, and the system is running on battery power, it will provide an audible alert with the remaining battery time and percentage.

## Configuration

You can modify the following variables in the `ups_monitor.py` file to customize the behavior:

- `CHECK_INTERVAL`: The interval (in seconds) between power status checks (default: 60)
- `ALERT_START_TIME`: The start time for audible alerts (default: "08:00")
- `ALERT_END_TIME`: The end time for audible alerts (default: "19:00")

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
