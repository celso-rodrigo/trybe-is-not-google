from pytest import raises
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    """Tests of Priority Queue"""

    priority_queue = PriorityQueue()

    value_1 = {
        "nome_do_arquivo": "mock1.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": None
    }

    value_2 = {
        "nome_do_arquivo": "mock2.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": None
    }

    value_3 = {
        "nome_do_arquivo": "mock3.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": None
    }

    priority_queue.enqueue(value_1)
    assert len(priority_queue) == 1
    assert priority_queue.search(0) == value_1

    priority_queue.enqueue(value_2)
    assert priority_queue.search(0) == value_2

    priority_queue.enqueue(value_3)
    assert priority_queue.search(2) == value_3
    assert len(priority_queue) == 3

    with raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(3)

    assert priority_queue.dequeue() == value_2
    assert priority_queue.dequeue() == value_1
    assert len(priority_queue) == 1
    