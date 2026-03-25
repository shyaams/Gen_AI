import os
import time

# Function to get system uptime

def get_uptime():
    # Get the uptime in seconds
    uptime_seconds = os.popen('cat /proc/uptime').read().split()[0]
    # Convert seconds to hours, minutes and seconds
    uptime_hours = int(float(uptime_seconds) // 3600)
    uptime_minutes = int((float(uptime_seconds) % 3600) // 60)
    uptime_seconds = int(float(uptime_seconds) % 60)
    return uptime_hours, uptime_minutes, uptime_seconds

# Main script
if __name__ == '__main__':
    hours, minutes, seconds = get_uptime()
    print(f'System Uptime: {hours} hours, {minutes} minutes, {seconds} seconds')