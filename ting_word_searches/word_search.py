from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    files = []

    for file in instance._data:
        filename = file["nome_do_arquivo"]
        lines = file["linhas_do_arquivo"]
        occurrences = [
            {"linha": line}
            for line, line_content in enumerate(lines, start=1)
            if word.lower() in line_content.lower()
        ]

        if occurrences:
            files.append({
                "palavra": word,
                "arquivo": filename,
                "ocorrencias": occurrences
            })

    return files


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
