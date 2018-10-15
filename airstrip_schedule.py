"""
airstrip_schedule.py
author: Marissa Allen

A class that will, in the future, keep track of the information needed to schedule the airstrip resource.
"""


class AirstripSchedule:     # Declaring placeholder variables.
    def __init__(self, plane_id, submission_time, requested_start, requested_duration, actual_start, actual_end):
        self.plane_id = plane_id
        self.submission_time = submission_time
        self.requested_start = requested_start
        self.requested_duration = requested_duration
        self.actual_start = 0       # initialized, will start at time slot 0 if !q.empty().
        self.actual_end = 0         #  and increment counter.


