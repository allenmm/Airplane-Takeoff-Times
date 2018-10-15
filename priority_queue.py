"""
priority_queue.py
author: Marissa Allen

A subclass for the Priority Queue class for custom ordering, since regular priority queues do not support it.
Each item that is placed into the queue generates a four-tuple. The first tuple element of the four-tuple takes
the second tuple element of the submitted item data and sets it as the highest priority element. The second tuple
element takes the third tuple element of the item data and sets it as the next highest priority. The third tuple
element of the four-tuple is added every time a new tuple item put into the queue. It is also incremented for
every item to further enforce the priority order.
"""
from queue import PriorityQueue
class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        """
        Creates an instance variable to avoid situations where the same item is placed in the queue.
        This insures that order will always be kept so no words or numbers take priority
        over the second and third tuple elements in the item.
        """
        PriorityQueue.__init__(self)
        self.increase = 0                # Initialize instance variable to zero.

    def put(self, item):
        """
        Puts an item into the queue as a four-tuple. The four-tuple will be sorted by priority by
        using the tuple item entry data that is submitted. When an item is put in, the second and third
        tuple elements are returned to the front of the queue, in that order, to establish custom
        ordering. Another variable is increased and added behind the those elements so all
        order is kept regardless of word and number ordering for the first item element.
        super() represents the parent class PriorityQueue.
        :param item: the item entered that is put into the tuple.
        """
        super().put((self.get_priority(item), self.get_nextpriority(item), self.increase, item))
        self.increase += 1                 # Adds a one onto the previous queue item for use in the current item.


    def get(self):
        """
        Removes the fourth element in the tuple and returns it to show what
        is the current highest priority item. If there are no elements left in the tuples
        it will print that the queue is empty.
        :return: removes and returns the fourth element in the tuple.
        """
        if len(self.queue) > 0:
            return super().get()[3]
        return ("The queue is empty!")


    def get_priority(self, item):
        """
        Sets the second element of the item to be the highest order priority.
        :param item: the item entered that is put into the tuple.
        :return: returns index to the first position of the four-tuple to establish priority.
        """
        return item[1]

    def get_nextpriority(self, item):
        """
        Sets the third element of the item to be the next highest order priority.
        :param item: the item entered that is put into the tuple.
        :return: Returns index to the second position in the four-tuple to establish priority.
        """
        return item[2]