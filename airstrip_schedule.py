"""
airstrip_schedule.py
author: Marissa Allen

Keeps track of the information needed to schedule the airstrip resource.
Adds an actual start time and actual end time to the AirstripSchedule
object as placeholders for later calculations.
"""


class AirstripSchedule:
    def __init__(self, plane_id, submission_time, requested_start,
                 requested_duration):
        """
        This is the common base class for all AirstripSchedule objects.
        It takes in the request identifier, request submission,
        time slot requested, and length of time requested from a nested
        list of string objects. Then adds an actual start time and actual
        end time to the AirstripSchedule object.
        :param plane_id: The request identifier string object.
        :param submission_time: The request submission string object.
        :param requested_start: The time slot requested string object.
        :param requested_duration: The length of time requested string
        object.
        """
        self.plane_id = plane_id
        self.submission_time = submission_time
        self.requested_start = requested_start
        self.requested_duration = requested_duration
        # Initialized to 0 as a placeholder
        # for later calculation.
        self.actual_start = 0
        # Initialized to 0 as a placeholder
        # for later calculation.
        self.actual_end = 0

    def __str__(self):
        """
        The __repr__ and __str__ functions are automatically created for
        every class. They are the two functions that control how objects
        are converted into strings in Python. This program uses a list,
        and lists always use the result of __repr__ to represent the
        objects they contain. But since it is good practice to define
        both of them, __repr__ is set to equal __str__ to return the
        object result when it is called.
        :return: formatted values of the request identifier, request
        submission, time slot requested, length of time requested, actual
        start time, and actual end time.
        """
        return self.plane_id + "," + self.submission_time + "," + \
               self.requested_start + "," + str(self.requested_duration) \
               + "," + str(self.actual_start) + "," + str(self.actual_end)

    # Sets __repr__ function to equal the __str__ function to convert
    # the object to a string.
    __repr__ = __str__

