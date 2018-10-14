"""
priority_queue.py
author: Marissa Allen

A subclass for the Priority Queue class for custom ordering, since regular priority queues do not support it.
The subclass makes the second element of a submitted item the highest priority and the third element
of that item the next highest priority. Another variable is added behind these elements and incremented
every time an item is added to the queue to further enforce the priority order.
"""
from queue import PriorityQueue
class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        """
        Creates an instance variable to avoid situations where the same item is put in the queue.
        This insures that order will always be kept so no words or numbers take priority
        over the second and third queue elements.
        """
        PriorityQueue.__init__(self)
        self.increase = 0                # Initialize instance variable to zero.

    def put(self, item):
        """
        Puts an item into the queue. When an item is put in the queue the second and third
        elements are returned to the front of the queue, in that order, to establish custom
        ordering. Another variable is increased and added behind the those elements so all
        order is kept regardless of word and number ordering for the first item element.
        super() represents the parent class PriorityQueue.
        :param item: the item entered that is put into the queue.
        """
        super().put((self.get_priority(item), self.get_nextpriority(item), self.increase, item))
        self.increase += 1                 # Adds a one onto the previous queue item for use in the current item.


    def get(self):
        """
        Pops off the fourth element in the queue to show what is the current
        highest priority item.
        :return: removes and returns the fourth element in the queue.
        """
        return super().get()[3]

    def get_priority(self, item):
        """
        Sets the second element of the item to be the highest order priority.
        :param item: the item entered that is put into the queue.
        :return: returns index to the front of the queue to establish priority.
        """
        return item[1]

    def get_nextpriority(self, item):
        """
        Sets the third element of the item to be the next highest order priority.
        :param item: the item entered that is put into the queue.
        :return: Returns index behind the second element at the front of the queue.
        """
        return item[2]
