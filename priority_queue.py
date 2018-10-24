"""
priority_queue.py
author: Marissa Allen

A subclass for the Priority Queue class for custom ordering, since regular
priority queues do not support it. This class enqueues the values from
each section of the class list in a seven-tuple. It establishes the
priority of the sections by using the request submission time as the
highest priority value, the time slot requested as the next highest
priority value, and the increase instance variable. And by placing the
request identifier, a repeat of the request submission time, a repeat of
the time slot requested, and length of time requested after the priority
values. To order the class list, it must be dequeued. The dequeue
function will return everything except the first three priority
values used to establish order.
"""
from queue import PriorityQueue
class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        """
        Creates an instance variable to avoid situations where the exact
        same request identifier, request submission, time slot
        requested, and length of time requested has been enqueued.
        This insures that order will always be kept so no words or numbers
        take priority over the request submission time and the time slot
        requested.
        """
        PriorityQueue.__init__(self)
        self.increase = 0          # Initialize instance variable to zero.

    def enqueue(self, req_id, high_priority, next_priority, duration):
        """
        Puts values from the class list into the queue as a seven-tuple
        to order values by priority. The queue is not sorted when it is
        enqueued. It is only sorted once it has been dequeued.
        The seven-tuple will be sorted by priority by using the request
        submission time as the highest priority value, the time slot
        requested as the next highest priority value, and the increase
        instance variable. The submission time (high_priority) is
        placed as the first value in the tuple, the the time slot
        requested (next_priority) is placed as the second value, and the
        increase variable is placed as the third. The fourth through
        seven values of the seven-tuple are then placed in order as:
        request identifier (req_id),
        request submission time (high_priority),
        time slot requested (next_priority), and length of time
        requested (duration).

        :param req_id: the request identifier value that is put into
        the tuple.
        :param high_priority: the request submission time that is put
        into the tuple.
        :param next_priority: the time slot requested that is put into
        the tuple.
        :param duration: the length of time requested that is put into
        the tuple.
        """
        # super() represents the parent class PriorityQueue.
        super().put((high_priority, next_priority, self.increase, req_id,
                     high_priority, next_priority, duration))
        # Adds a one onto the previous queue item for use in the
        # current item.
        self.increase += 1


    def dequeue(self):
        """
        Orders the list of class values by removing them from the queue.
        Removes index three through six of the values that were enqueued
        in the tuple. It then returns these indexes as a four-tuple.
        It does this for each section of the class list that was enqueued.
        The values are dequeued based on their priority. If there are no
        elements left in the tuples it will print that the queue is empty.
        :return: removes and returns index three through six in the
        enqueued tuple.
        """
        if len(self.queue) > 0:
            return super().get()[3:7]
        return "The queue is empty"

    def peek(self):
        """
        Lets you look at the first value that is currently in the
        queue.
        :return: a line stating that you can't peek when there are no
        values in the queue.
        """
        if len(self.queue) > 0:
            return self.queue[0][3:7]
        return "Cannot peek when queue is empty"
