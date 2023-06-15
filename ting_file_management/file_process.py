from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
