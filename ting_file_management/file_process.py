from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    # Verifica se o arquivo já está na instância
    for file in instance._data:
        if file["nome_do_arquivo"] == path_file:
            return None

    # Lê as linhas do arquivo
    lines = txt_importer(path_file)

    # Cria um dicionário com as informações do arquivo
    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    # Adiciona o novo dicionário à instância
    instance.enqueue(new_dict)

    # Imprime o dicionário
    print(new_dict)


def remove(instance: Queue):
    # Verifica se há elementos na instância
    if len(instance._data) <= 0:
        print("Não há elementos")
        return None

    # Remove o arquivo da instância e obtém o nome do arquivo removido
    removed = instance.dequeue()["nome_do_arquivo"]

    # Imprime a mensagem de sucesso com o nome do arquivo removido
    print(f"Arquivo {removed} removido com sucesso")


def file_metadata(instance: Queue, position: int):
    try:
        # Busca o arquivo na posição especificada na instância
        file = instance.search(position)

        # Imprime as informações do arquivo
        print(file)
    except IndexError:
        # Se a posição for inválida, exibe uma mensagem de erro
        sys.stderr.write("Posição inválida\n")
