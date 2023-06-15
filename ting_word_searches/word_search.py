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


def search_by_word(word: str, instance: Queue):
    files = []

    for index in range(len(instance)):
        actual_file = instance.search(index)
        file_finded = {
            "palavra": word,
            "arquivo": actual_file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for index_second, line in enumerate(actual_file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                file_finded["ocorrencias"].append(
                    {
                        "linha": index_second + 1,
                        "conteudo": line
                    }
                )
        if file_finded["ocorrencias"]:
            files.append(file_finded)

    return files
