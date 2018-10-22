"""
airstrip_schedule.py
author: Marissa Allen

A class that will, in the future, keep track of the information needed to schedule the airstrip resource.
"""


class AirstripSchedule:
    def __init__(self, plane_id, submission_time, requested_start, requested_duration):
        self.plane_id = plane_id
        self.submission_time = submission_time
        self.requested_start = requested_start
        self.requested_duration = requested_duration
        self.actual_start = 0
        self.actual_end = 0

    def __str__(self):
        return self.plane_id + "," + self.submission_time + "," + self.requested_start + "," + str(self.requested_duration) \
               + "," + str(self.actual_start) + "," + str(self.actual_end)

    __repr__ = __str__          #

