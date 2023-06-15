from pathlib import Path
import sys


def txt_importer(path_file):
    file = Path(path_file)

    # Verifica se o formato do arquivo é válido
    if file.suffix != ".txt":
        sys.stderr.write("Formato inválido\n")
        return None

    # Verifica se o arquivo existe
    if not file.exists():
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return None

    # Lê as linhas do arquivo
    with open(path_file, "r") as file:
        lines = [line.rstrip() for line in file]

    return lines
