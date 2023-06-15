from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    customer_first = {
        "nome_do_arquivo": "arquivo 01",
        "qtd_linhas": 1,
        "linhas_do_arquivo": ["test1", "test2", "test3", "test4"]
    }

    customer_second = {
        "nome_do_arquivo": "arquivo 02",
        "qtd_linhas": 6,
        "linhas_do_arquivo": ["test1", "test2", "test3", "test4"],
    }

    customer_third = {
        "nome_do_arquivo": "arquivo 03",
        "qtd_linhas": 8,
        "linhas_do_arquivo": ["test1", "test2", "test3", "test4"],
    }

    customer_fourth = {
        "nome_do_arquivo": "arquivo 04",
        "qtd_linhas": 7,
        "linhas_do_arquivo": ["test1", "test2", "test3", "test4"],
    }

    priority_queue = PriorityQueue()

    priority_queue.enqueue(customer_first)
    priority_queue.enqueue(customer_second)
    priority_queue.enqueue(customer_third)

    assert len(priority_queue) == 3

    assert priority_queue.search(2)["qtd_linhas"] == 8
    assert priority_queue.search(0)["qtd_linhas"] == 1
    assert priority_queue.search(1)["qtd_linhas"] == 6

    priority_queue.dequeue()

    priority_queue.enqueue(customer_fourth)

    assert len(priority_queue.regular_priority) == 3
    assert len(priority_queue.high_priority) == 0

    with pytest.raises(IndexError):
        priority_queue.search(100)

    with pytest.raises(IndexError):
        priority_queue.search(200)
