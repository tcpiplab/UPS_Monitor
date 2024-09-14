import os
import time
import psutil
from datetime import datetime

def check_power_status():
    battery = psutil.sensors_battery()
    if battery:
        # Uncomment for testing with inverse logic
        # if battery.power_plugged:
        if not battery.power_plugged:
            alert_user(battery)
    else:
        print("No battery information available.")

def alert_user(battery):
    current_time = datetime.now().time()
    if current_time >= datetime.strptime("08:00", "%H:%M").time() and current_time <= datetime.strptime("19:00", "%H:%M").time():
        remaining_time = battery.secsleft / 60  # Convert seconds to minutes
        battery_percentage = battery.percent

        print(f"Remaining Time: {remaining_time}")

        if remaining_time < 0:
            remaining_time_str = "Unlimited (charging)"
        elif remaining_time == psutil.POWER_TIME_UNKNOWN:
            remaining_time_str = "Unknown"
        else:
            remaining_time_str = f"{remaining_time:.0f} minutes"


        
        alert_message = f"Power outage detected! Running on battery power. {battery_percentage}% battery remaining, approximately {remaining_time_str} left."
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - {alert_message}")
        os.system(f'say "{alert_message}"')  # This will speak the alert message on macOS.
    else:
        print(f"Power outage detected, but no audible alert due to time restrictions. Current time: {current_time}")

if __name__ == "__main__":
    while True:
        check_power_status()
        time.sleep(60)  # Check every 60 seconds