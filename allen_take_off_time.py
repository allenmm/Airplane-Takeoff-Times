"""
allen_take_off_time.py
author: Marissa Allen

allen_take_off_time is a program that takes in a file pathname the user submits from the terminal, reads the file lines, stores
the lines in a list as strings split by commas, and passes those into another function/class to be...
"""

import sys
from queue import PriorityQueue
import priority_queue

def file_read(user_file):
    """
    Reads the file for the airplane requests. When a text file is submitted by the user the program tries to open
    the file. A file object is created when the file successfully opens...
    If the file fails to open, a message will print to the terminal, saying that the program could not read the file
    and ask the user to submit another file.

    :param user_file: contains a command line argument file pathname that the user submitted.
    :return: Returns the list to the function call.
    """

    try:
        file = open(user_file, 'r')          # Tries to open the user's text file.
    except Exception:                        # If the file open fails it tells the user to submit another text file.
        print("\nCould not read the file or directory:", sys.argv[1])
        print("Please submit a valid text file to the program.\n")
        print("Example: test.txt is a valid file name.\n")
        sys.exit()                                              # Exits Python, program does not raise SystemExit and returns.
    readlines = file.read().splitlines()                        # Reads content of the text file and returns a list with all the lines in a string.
    file.close()                                                # Flushes unwritten information from the file and closes it.
    schedule_list = [line.split(", ") for line in readlines]    # Seperates strings into a list containing one line per element.
    return schedule_list


def main(user_file):
    """
    Passes the file pathname to the file_read function and stores its return value for future use.
    :param user_file: contains a command line argument file pathname that the user submitted.
    """
    plane_list = file_read(user_file)   # Stores value of file.

if __name__ == '__main__':  # Runs if we're running the program directly from this file.
    main(sys.argv[1])       # Calls main function, passes in user text file.
