import sys


def txt_importer(path_file):
    """
    Receives a path and returns a list with the content of the .txt
    file on that path. If the file does not exist or is not a .txt
    file, an error message will be printed.
    """

    if not path_file.endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file, "r") as file:
            content_file = file.read()
            return list(content_file.split("\n"))
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
