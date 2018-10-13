# allen_take_off_time.py
# Author: Marissa Allen
"""
    Insert file description here.
"""

import sys
from queue import PriorityQueue


def file_read(user_file):
    """
        Reads a file for the airplane requests. When a text file is submitted by the user...
        
    """
    
    try:
        file = open(user_file, 'rt')      # Tries to open the user's text file.
    except Exception:                     # If the file open fails it tells the user to submit another text file.
        print("\nCould not read the file or directory:", sys.argv[1])
        print("Please submit a valid text file to the program.")
        print("Example: test.txt is a valid file name.\n")
        sys.exit()
    readlines = file.read().splitlines()                          # Reads the content of the text file and returns a list with all the lines in a string.
    file.close()                                                  # Flushes unwritten information from the file and closes it.
    schedule_list = [line.split(", ") for line in readlines]      # Seperates strings into a list containing one line per element.
    print(schedule_list)                                          # Test print list.
    return schedule_list                                          # Returns the list to the function call.


def plane_queue(self):
    """ 
    Pydoc comments go under all functions. 
    """



def main(user_file):
    """
    Pydoc comments go under all functions.
    """
    # print("This is a test of the emergency broadcast system. ")
    schedule_list = file_read(user_file)


if __name__ == '__main__':          # Running the code from this module, this main, if we're running the program directly from this file.
    main(sys.argv[1])                          # Calls main function.
