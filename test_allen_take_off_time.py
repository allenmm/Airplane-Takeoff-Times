"""
test_allen_take_off_time.py
author: Marissa Allen

File for unit testing. Tests to make sure that all functions function
properly. Currently tests the class_requests function and
sorted_requests function in allen_take_off_time and the functions
in the priority queue subclass in priority_queue.

"""

import allen_take_off_time
import priority_queue


def test_main():
    """
    Tests if the functions correctly accept the data that is entered.
    """

    q = priority_queue.MyPriorityQueue()
    q.enqueue(1, 5, 5, 0)
    q.enqueue(2, 2, 5, 0)
    q.enqueue(2, 1, 5, 0)
    test1 = q.empty()
    print("Should be false: ", test1)
    print("Ordered by second element test. "
          "Below should be (2, 1, 5, 0) (2, 2, 5, 0) (1, 5, 5, 0):")
    print(q.dequeue(), q.dequeue(), q.dequeue(), "\n")
    test2 = q.empty()
    print("Should be true: ", test2)
    q.enqueue('delta 70', 1, 3, 0)
    q.enqueue('ual 7', 1, 2, 0)
    q.enqueue(3, 2, 5, 0)
    q.enqueue(2, 2, 7, 0)
    q.enqueue(2, 1, 5, 0)
    q.enqueue('ual 80', 1, 5, 0)
    q.enqueue(2, 1, 5, 0)
    print("Peek should be '('ual 7', 1, 2, 0)':", q.peek())
    print("Ordered by second and third element test. "
          "Below should be: ('ual 7', 1, 2, 0), ('delta 70', 1, 3, 0), "
          "(2, 1, 5, 0), ('ual 80', 1, 5, 0), (2, 1, 5, 0), (3, 2, 5, 0), "
          "(2, 2, 7, 0)")
    while not q.empty():
        print(q.dequeue())
    test3 = q.empty()
    print("Should be true: ", test3)
    print("Test for if dequeue() is called after queue is empty. "
          "Should say 'The queue is empty': ", q.dequeue())
    print("Test for if peek() is called after queue is empty. "
          "Should say 'Cannot peek when queue is empty':", q.peek())

    class_test_list = [['Delta 170', '9', '10', '2'],
                       ['UAL 7','1', '2', '1']]
    print("\nTest to see if it accepts nested list of string objects and "
          " adds them to the class",
          "\nShould be [Delta 170,9,10,2,0,0, UAL 7,1,2,1,0,0]: ",
          allen_take_off_time.class_requests(class_test_list))

    print("\nTest to see if it accepts a list of class objects "
          "and orders them."
          "\nShould be [('UAL 7', '1', '2', '1'), "
          "('Delta 170', '9', '10', '2')]: ", )
    pq_test_list = allen_take_off_time.class_requests(class_test_list)
    print(allen_take_off_time.sorted_requests(pq_test_list))



if __name__ == '__main__':
    test_main()
