# Create a log file to keep track of the script's execution or if it exists load it
import os
import datetime
import sys
import time

# Ensure all packages in requirements.txt are installed
os.system('pip3 install -r requirements.txt')

boolean = False

# Read file or create it if it doesn't exist
if os.path.exists('log.txt'):
    log = open('log.txt','a')

    # Get current date and time
    now = datetime.datetime.now()

    # Get the contents of the log file
    log_contents = log.read()

    # Convert the contents of the log file to a datetime object
    log_contents = datetime.datetime.strptime(log_contents,'%Y-%m-%d %H:%M:%S.%f')

    # Get the difference between the current time and the time the script was last run
    difference = now - log_contents

    # If the difference is greater than 24 hours, run the script
    if difference.days >= 1:
        boolean = True
else:
    boolean = True

# If the script should be run, run it
if boolean:
    # run driver.py
    result = os.system('python3 driver.py')

    # See if code 0 was returned
    if result == 0:
        # Get current date and time
        now = datetime.datetime.now()

        # Overwrite the log file with the current date and time
        log = open('log.txt','w')
        log.write(str(now))
        log.close()
    else:
        # If the script failed to run, print an error message
        print('The script failed to run')
else:
    # If the script should not be run, print a message
    print('The script should not be run')

