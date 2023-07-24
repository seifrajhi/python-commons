import os
import subprocess
import time

print("Dynamically waiting for Ubuntu's automatic update mechanism to let go of locks...")

time.sleep(15)  # In case this script is the very first command being run, we wait a bit to give unattended upgrades a chance to start.

while True:
    if not os.path.exists("/var/lib/apt/lists/lock"):
        break
    print("waiting")
    time.sleep(1)

while True:
    if not os.path.exists("/var/lib/dpkg/lock"):
        break
    print("still waiting")
    time.sleep(1)

print("All locks should have been released...")
