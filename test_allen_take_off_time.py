"""
test_allen_take_off_time.py
author: Marissa Allen

File for unit testing. Tests to make sure that all functions function properly.
Currently tests the file_read function in allen_take_off_time and the functions
in the priority queue subclass in priority_queue.

"""

import sys
import allen_take_off_time
import priority_queue


def test_main():
    """
    Tests if the classes and functions correctly accept the data that is entered.
    """

    q = priority_queue.MyPriorityQueue()
    q.enqueue(1, 5, 5, 0)
    q.enqueue(2, 2, 5, 0)
    q.enqueue(2, 1, 5, 0)
    test1 = q.empty()
    print("\nThis is the priority queue: ",q.queue, "\n")
    print("Should be false: ", test1)
    print("Ordered by second element test. Below should be (2, 1, 5, 0) (2, 2, 5, 0) (1, 5, 5, 0):")
    print(q.dequeue(), q.dequeue(), q.dequeue(), "\n")
    test2 = q.empty()
    print("Should be true: ", test2)
    q.enqueue('delta 70', 1, 3, 0)
    q.enqueue('ula 7', 1, 2, 0)
    q.enqueue(3, 2, 5, 0)
    q.enqueue(2, 2, 7, 0)
    q.enqueue(2, 1, 5, 0)
    q.enqueue('ula 80', 1, 5, 0)
    q.enqueue(2, 1, 5, 0)
    print("Peek should be '('ula 7', 1, 2, 0)':", q.peek())
    print(q.queue)
    print("Ordered by second and third element test. Below should be: ('ula 7', 1, 2, 0), ('delta 70', 1, 3, 0), "
          "(2, 1, 5, 0), ('ula 80', 1, 5, 0), (2, 1, 5, 0), (3, 2, 5, 0), (2, 2, 7, 0)")
    while not q.empty():
        print(q.dequeue())
    test3 = q.empty()
    print("Should be true: ", test3)
    print("Test for if dequeue() is called after queue is empty. Should say 'The queue is empty': ", q.dequeue())
    print("Test for if peek() is called after queue is empty. Should say 'Cannot peek when queue is empty':", q.peek())

    actual = allen_take_off_time.file_read(sys.argv[1])       # for if file accept test passes.
    print("\nShould print a nested list of the text file containing one string line per element: ", actual)
    print("\nShould say: 'Could not read the file or directory: 'filename' ",
          "Please submit a valid text file to the program. Example: test.txt is a valid file name.': ")
    allen_take_off_time.file_read('test1.txt')  # for if file accept test fails. Print test is above.


if __name__ == '__main__':
    test_main()
