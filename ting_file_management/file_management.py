from pathlib import Path
import sys


def txt_importer(path_file):
    file = Path(path_file)
    if not file.endswith(".txt"):
        return None

    if not file.exists():
        print(f"Arquivo {file} não encontrado", file=sys.stderr)
        return None
