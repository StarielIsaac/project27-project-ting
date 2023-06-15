from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data += 1

    def dequeue(self):
        self._data += 1

    def search(self, index):
        """Aqui irá sua implementação"""