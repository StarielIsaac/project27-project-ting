from pathlib import Path
import sys


def txt_importer(path_file):
    file = Path(path_file)
    if file.suffix != ".txt":
        sys.stderr.write("Formato inválido\n")
        return None

    if not file.exists():
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return None

    with open(path_file, "r") as file:
        lines = [line.rstrip() for line in file]

    return lines
