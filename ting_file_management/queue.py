from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    # Inicializa a lista vazia para armazenar os elementos da fila
    def __init__(self):
        self._data = []

    # Retorna o tamanho da fila
    def __len__(self):
        return len(self._data)

    # Adiciona um elemento ao final da fila
    def enqueue(self, value):
        self._data.append(value)

    # Remove e retorna o primeiro elemento da fila
    def dequeue(self):
        # Retorna None se a fila estiver vazia
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    # Retorna o elemento correspondente ao índice fornecido
    def search(self, index):
        # Lança uma exceção se o índice estiver fora dos limites da fila
        if index < 0 or index >= len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]
