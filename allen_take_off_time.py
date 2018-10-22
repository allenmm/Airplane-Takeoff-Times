"""
allen_take_off_time.py
author: Marissa Allen

allen_take_off_time is a program that takes in a file pathname the user submits from the terminal, reads the file lines,
stores the lines into a list, and will pass those into a priority queue to be ordered.
"""

import sys
import priority_queue
import airstrip_schedule


def file_read(user_file):
    """
    Reads the file for the airplane requests. When a text file is submitted by the user the program tries to open
    the file. A file object is created when the file successfully opens, the file content is split by commas, and stored
    in a list with each section as a string element to be passed into a function in the future and ordered by a priority
    queue. If the file fails to open, a message will print to the terminal, saying that the program could not read the
    file and ask the user to submit another file.

    :param user_file: contains a command line argument file pathname that the user submitted.
    """

    try:
        file = open(user_file, 'r')          # Tries to open the user's text file.
    except Exception:                        # If the file open fails it tells the user to submit another text file.
        print("\nCould not read the file or directory:", sys.argv[1])
        print("Please submit a valid text file to the program\n")
        print("Example: test.txt is a valid file name\n")
        sys.exit()                                              # Exits Python, program does not raise SystemExit and returns.
    readlines = file.read().splitlines()                        # Reads content of the text file and returns a list with all the lines in a string.
    file.close()                                                # Flushes unwritten information from the file and closes it.
    schedule_list = [line.split(", ") for line in readlines]    # Seperates strings into a list containing one line per element.
    print(class_requests(schedule_list))


def class_requests(new_list2):
    """
    Creates a list of class objects as long as the requested start time isn't earlier than the submission time.
    :param new_list2:
    :return:
    """


    new_list = []
    for new_list2 in new_list2:
        if int(new_list2[2]) < int(new_list2[1]):
            print("\nYour requested start time,", new_list2[2], "cannot be earlier than your submission time", new_list2[1])
            print("The error is in the section:", new_list2,
                  "\nPlease resubmit the file after fixing the error")
            sys.exit()
        new_list.append(airstrip_schedule.AirstripSchedule(plane_id=new_list2[0], submission_time=new_list2[1],
                                                           requested_start=new_list2[2], requested_duration=new_list2[3]))
    return new_list


def main(user_file):
    """
    Passes the file pathname to the file_read function and stores its return value for future use.
    :param user_file: contains a command line argument file pathname that the user submitted.
    """

    file_read(user_file)

if __name__ == '__main__':  # Runs if we're running the program directly from this file.
    main(sys.argv[1])       # Calls main function, passes in user text file.
