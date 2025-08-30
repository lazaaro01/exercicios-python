import pytest
from queue import Queue

def test_enqueue_and_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty()

def test_peek():
    q = Queue()
    q.enqueue('a')
    assert q.peek() == 'a'
    q.enqueue('b')
    assert q.peek() == 'a'

def test_is_empty():
    q = Queue()
    assert q.is_empty()
    q.enqueue(10)
    assert not q.is_empty()

def test_dequeue_empty_queue():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()

def test_peek_empty_queue():
    q = Queue()
    with pytest.raises(IndexError):
        q.peek()
