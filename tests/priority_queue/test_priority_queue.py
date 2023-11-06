from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    data1 = {"nome_do_arquivo": "file1.txt", "qtd_linhas": 3}
    data2 = {"nome_do_arquivo": "file2.txt", "qtd_linhas": 6}

    # Test enqueue and dequeue operations
    priority_queue.enqueue(data1)
    priority_queue.enqueue(data2)

    assert priority_queue.dequeue() == data1
    assert priority_queue.dequeue() == data2

    # Test the length of the queue
    assert len(priority_queue) == 0

    priority_queue.enqueue(data1)
    assert len(priority_queue) == 1

    priority_queue.enqueue(data2)
    assert len(priority_queue) == 2

    priority_queue.dequeue()
    assert len(priority_queue) == 1

    # Test the search method
    priority_queue.enqueue(data1)
    priority_queue.enqueue(data2)

    assert priority_queue.search(0) == data1
    assert priority_queue.search(1) == data2

    # Test searching for an index out of range
    pytest.raises(IndexError, priority_queue.search, 3)
