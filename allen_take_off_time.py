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
    in a list with each section as a string element to be passed into the plane_requests function. If the file fails to open, a message will print to the terminal, saying that the program could not read the
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
    plane_requests(schedule_list)


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


def sorted_requests(new_list):
    """

    :param new_list:
    :return:
    """

    list2 = []

    pq = priority_queue.MyPriorityQueue()

    for i in new_list:
        if int(i.requested_duration) < 1:
            print("\nYour requested duration time,", i.requested_duration, "cannot be smaller than 1.")
            print("Planes must be on the runway for at least one time slot")
            print("The error is in the section:", "[", i.plane_id, ",", i.submission_time, ",", i.requested_start,
                  ",", i.requested_duration, "]"
                  "\nPlease resubmit the file after fixing the error")
            sys.exit()
        else:
            pq.enqueue(i.plane_id, i.submission_time, i.requested_start, i.requested_duration)
    print("Before PQ: ", pq.queue)
    while not pq.empty():               # sorts the list by their submission and requested start time.
        list2.append(pq.dequeue())      # now it's put into a list.
    print("After PQ:", list2)
    return list2


def plane_requests(schedule_list):
    """

    :param schedule_list:
    """

    print("File list: ", schedule_list)
    request_list = schedule_list
    request_list = class_requests(request_list)  # Passes in plane requests to be loaded into the class.
    print("unordered class: ", request_list)
    request_list = sorted_requests(request_list)    # Passes in plane requests to PQ to be sorted.
    ordered_list = class_requests(request_list)
    print("Ordered class:", ordered_list)

    print("Before actual start change: ", ordered_list[0].actual_start)
    ordered_list[0].actual_start = ordered_list[0].requested_start # gonna give it its request time cause it's at the front of queue
    ordered_list[0].actual_end = (int(ordered_list[0].requested_duration)-1)
    print("After actual start change: ", ordered_list[0].actual_start)
    print("Before change: ", ordered_list)
    for i in range(1, len(ordered_list)):   # from 1 to length of request
        ordered_list[i].actual_start = int(ordered_list[i-1].actual_start) + int(ordered_list[i-1].requested_duration)
        print("After request: ", ordered_list)
        ordered_list[i].actual_end = int(ordered_list[i].actual_start) + (int(ordered_list[i].requested_duration)-1)
        print("After duration: ", ordered_list)

    print(final_times(ordered_list))    # or print from main


def final_times(ordered_list):

    values = ""     # Initializing return value
    for i in range(len(ordered_list)):
        plane_id = ordered_list[i].plane_id
        actual_start = ordered_list[i].actual_start
        actual_end = ordered_list[i].actual_end
        if i == len(ordered_list)-1:
            values += str(plane_id) + " (" + str(actual_start) + "-" + str(actual_end) + ")"
        else:
            values += str(plane_id) + " (" + str(actual_start) + "-" + str(actual_end) + "), "
    return values


def main(user_file):
    """
    Takes in a file pathname and passes it to the file_read function to be used in the program.
    :param user_file: contains a command line argument file pathname that the user submitted.
    """

    file_read(user_file)


if __name__ == '__main__':  # Runs if we're running the program directly from this file.
    main(sys.argv[1])       # Calls main function, passes in user text file.
