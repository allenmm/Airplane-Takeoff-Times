"""
allen_take_off_time.py
author: Marissa Allen

allen_take_off_time is a program that takes in a file pathname the user
submits from the terminal, reads the file lines, stores the lines into a
list. Then it will pass that list into a function that creates a list of
class objects by loading the list into the class constructor. This list is
then passed and enqueued into a priority queue function to order the
list of class files. It will then pass the list from the priority queue
one more time through the class list function to produce a sorted class
list. The actual start and actual end times will be calculated from the
sorted class list values and reassigned per list section for those
values. Then the list will be passed to the final_times function to print
out the queue status for every time slot and to the print_format function
to print a formatted string of actual take off times.

Where n is any number within the range of the list:
ordered_list[n].actual_start - represents the actual start time of the
class list section.
ordered_list[n].requested_start - represents the requested start time
of the class list section.
ordered_list[n].requested_duration - represents the requested
duration time of the class list section.
ordered_list[n].actual_end - represents the actual end time of the
class list section.
"""

import sys
import priority_queue
import airstrip_schedule


def file_read(user_file):
    """
    Reads the file for the airplane requests. When a text file is
    submitted by the user the program tries to open the file. A file
    object is created when the file successfully opens, the file content
    is split by commas, and a for loop is used to store this file
    content in a list with each section as a string element to be passed
    into the plane_requests function. If the file fails to open,
    a message will print to the terminal, saying that the program
    could not read the file and ask the user to submit another file.

    :param user_file: contains a command line argument file pathname that
    the user submitted.
    """

    try:
        file = open(user_file, 'r')  # Tries to open the user's text file.
    # If the file open fails it tells the user to submit another text file.
    except Exception:
        print("\nCould not read the file or directory:", sys.argv[1])
        print("Please submit a valid text file to the program\n")
        print("Example: test.txt is a valid file name\n")
        # Exits Python, program does not raise SystemExit and returns.
        sys.exit()
    # Reads content of the text file and returns a list with all
    # the lines in a string.
    readlines = file.read().splitlines()
    # Flushes unwritten information from the file and closes it.
    file.close()
    # Separates strings into a list containing one line per element.
    schedule_list = [line.split(", ") for line in readlines]
    # Passes list of strings.
    plane_requests(schedule_list)


def class_requests(request_list):
    """
    Creates a list of class objects by using a for loop to take in a
    nested list of string objects and passing the plane identifier,
    request submission time, time slot request, and length of time
    requested values for every sublist into the AirstripSchedule class.
    It will then append the returned AirstripSchedule objects inside of
    a new list and return a new list of class objects. This returned
    list of class objects is not in sorted order.

    :param request_list: A nested list of string objects that represent
    the text file the user entered.
    :return: returns a list of class objects taken from the nested list
    of string objects, along with an actual start time and end time as
    a list of class objects.
    """

    class_list = []            # Initializing return value.
    for request_list in request_list:
        # Stores the plane identifier of each string object in plane_id.
        plane_id = request_list[0]
        # Stores the request submission time of each string object
        # in submission_time.
        submission_time = request_list[1]
        # Stores the time slot request of each string object
        # in requested_start.
        requested_start = request_list[2]
        # Stores the length of time requested of each string object
        # in requested_duration.
        requested_duration = request_list[3]
        # Takes in values for the class and appends returned values
        # to a list.
        class_list.append(airstrip_schedule.
                          AirstripSchedule(plane_id,submission_time,
                                           requested_start,
                                           requested_duration))
    return class_list    # returns appended list of class objects.


def sorted_requests(request_list):
    """
    Creates a list of ordered string objects from a list of class values.
    Using a for loop, the values from the list of class objects is
    enqueued in a priority queue. The queue is not in sorted order until
    it is dequeued. So, a while loop is used to dequeue the values,
    append them to a list as they are dequeued. The returned list is
    now in sorted order.

    :param request_list: A list of class objects that need to be ordered
    by the priority queue.
    :return: A list of string objects containing class object values that
    have now been ordered.
    """

    pq_list = []     # Initializing return value.

    # Creates a MyPriorityQueue object.
    pq = priority_queue.MyPriorityQueue()
    for i in request_list:
        pq.enqueue(i.plane_id, i.submission_time, i.requested_start,
                   i.requested_duration)
    # The class objects must be dequeued in order to be ordered.
    while not pq.empty():
        # Ordered object elements are now put into a list to be returned.
        pq_list.append(pq.dequeue())
    return pq_list          # returns appended list of string objects.


def plane_requests(schedule_list):
    """
    Takes in a nested list of string objects and passes them into the
    class_requests function, returning an unordered list of class
    objects. Then it passes that list into the sorted_requests function
    to return an ordered list of string objects. This ordered list is
    then passed back into the class_requests function to return an
    ordered list of class values. The ordered list of class values are
    used to calculate the actual start time and actual end time for the
    first section of the class list. Every other section of the class list
    uses the start and end times from the first section of the list for
    the actual start and actual end time calculations. It then passes
    the ordered class list and a time variable as parameters to the
    final_times function and prints out the queue status for every time
    slot. And passes the same class list into the print_format function
    to print the returned formatted string of actual take off times.

    Where n is any number within the range of the list:
    ordered_list[n].actual_start - represents the actual start time of the
    class list section.
    ordered_list[n].requested_start - represents the requested start time
    of the class list section.
    ordered_list[n].requested_duration - represents the requested
    duration time of the class list section.
    ordered_list[n].actual_end - represents the actual end time of the
    class list section.
    :param schedule_list: A nested list of string objects that represent
    the text file the user entered.
    """
    request_list = schedule_list   # Renames the parameter.
    # Passes in the plane requests to be loaded into the class and stores
    # the unordered list as the request_list value.
    request_list = class_requests(request_list)
    # Passes in plane requests to the priority queue function
    # to be sorted.
    request_list = sorted_requests(request_list)
    # Passes in an ordered list of plane requests to be loaded into the
    # class and stores the ordered list as the ordered_list value.
    ordered_list = class_requests(request_list)
    # The request time for the first section of the ordered class list
    # is assigned the requested start time it asked for. What ever the
    # section's request time is, it is given to it because it's at the
    # front of queue.
    ordered_list[0].actual_start = ordered_list[0].requested_start
    # The actual end time for the first section of the ordered class list
    # is calculated by subtracting one from the requested duration time
    # and assigning it to be the new actual end time.
    ordered_list[0].actual_end = \
        (int(ordered_list[0].requested_duration)-1)
    # From one to the length of request it calculates the actual start
    # and end times of the list sections.
    for i in range(1, len(ordered_list)):
        # Calculating the actual start time of the
        # class list section.
        ordered_list[i].actual_start = \
            int(ordered_list[i-1].actual_start) + \
            (int(ordered_list[i-1].requested_duration))
        # Calculating the actual end time of the
        # class list section.
        ordered_list[i].actual_end = \
            int(ordered_list[i].actual_start) + \
            (int(ordered_list[i].requested_duration)-1)

    # Compensates for the offset.
    for i in range(1, len(ordered_list)):
        ordered_list[i].actual_start = (int(ordered_list[
                                                i].actual_start)-1)
        ordered_list[i].actual_end = (int(ordered_list[i].actual_end)-1)

    print(ordered_list)
    list_length = len(ordered_list)   # Length of the list.
    # Calculates the number of time slots by getting the last list value's
    # actual end time.
    time_slot_count = ordered_list[list_length-1].actual_end
    time = 0
    while time <= time_slot_count:
        print(print_format(ordered_list, time), "\n")
        time += 1
    # Prints out the formatted string of actual take off times for planes.
    #print(final_times(ordered_list))   #uncomment when done with other.


def print_format(ordered_list, time):
    """
    Takes in a list of AirstripSchedule objects and a time integer for
    the time slots. And formats them to display the plane identifier and
    actual start time values from the list of class objects along with
    the time slot values, to return a string of values displaying the
    queue status.

    :param ordered_list: A list of ordered class objects to pull the
    status of the queue from.
    :param time: An integer number that keeps track of the time slot the
    queue status is on.
    :return: A list of formatted string values containing the queue status.
    """

    for i in range(len(ordered_list)):
        value = "At time " + str(time) + " the queue would look like: "
        plane_id = ordered_list[i].plane_id
        submission_time = ordered_list[i].submission_time
        actual_start = ordered_list[i].actual_start
        actual_end = ordered_list[i].actual_end


        # Checks to see if the first value is going to start at time slot
        # 0 or be scheduled for later. The first value is always only
        # going to have one because there can only be one plane on the
        # runway at a time.
        if time == 0:
            if time >= int(actual_start):
                value += str(plane_id) + " (started at " + \
                             str(actual_start) + ")"
            else:
                value += str(plane_id) + " (scheduled for " + \
                             str(actual_start) + ")"
            return value
        if time >= int(actual_start) & time >= int(submission_time) & \
                time == 3:
                value += str(plane_id) + " (started at " + \
                             str(actual_start) \
                             + "), "

        if time < int(actual_end):
            value += str(plane_id) + " (scheduled at " + \
                     str(actual_start) \
                     + "), "
            return value
        else:
            value += str(plane_id) + " (scheduled for " + \
                             str(actual_start) + "), "

    return value

def final_times(ordered_list):
    """
    Takes in a list of AirstripSchedule objects and formats them to
    display the plane identifier, actual start time, and actual end
    time values from the list of class objects to return a string of
    take off values. The for loop goes through the sections of the class
    list, and stores the values from the list of class objects, and
    returns the formatted string to its function call. The if and else
    statement in the for loop are for formatting looks. These statements
    append the list of values to each other with a comma at the end of
    every list section as it goes through the for loop, except for the
    last section. The last section of the list will be appended to the
    return string without a comma.

    :param ordered_list: A list of ordered class objects to pull the take
    off values from.
    :return: returns a list of formatted string values containing the
    actual take off times for the planes.
    """
    take_off_values = ""    # Initializing return value
    for i in range(len(ordered_list)):
        # Stores the plane identifier of each class object in plane_id.
        plane_id = ordered_list[i].plane_id
        # Stores the actual start time of each class object in
        # actual_start.
        actual_start = ordered_list[i].actual_start
        # Stores the actual end time of each class object in actual_end.
        actual_end = ordered_list[i].actual_end
        # For formatting to remove the comma from the last list section.
        if i == len(ordered_list)-1:
            take_off_values += str(plane_id) + " (" + str(actual_start) +\
                               "-" + str(actual_end) + ")"
        else:
            take_off_values += str(plane_id) + " (" + str(actual_start) +\
                               "-" + str(actual_end) + "), "
    return take_off_values


def main(user_file):
    """
    Takes in a file pathname and passes it to the file_read function to
    be used in the program.

    :param user_file: contains a command line argument file pathname that
    the user submitted.
    """

    file_read(user_file)


# Runs if we're running the program directly from this file.
if __name__ == '__main__':
    # Calls the main function, passes in user text file.
    main(sys.argv[1])
