from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Creates a new queue"""
        self._data = list()

    def __len__(self):
        """Returns the size of the list"""
        return len(self._data)

    def enqueue(self, value):
        """Add a new value to the end of the queue"""
        self._data.append(value)

    def dequeue(self):
        """Removes the first element of the queue"""
        if self.__len__() == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        """Returns the value at the chosen index"""
        if index < 0 or index > self.__len__() - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]
