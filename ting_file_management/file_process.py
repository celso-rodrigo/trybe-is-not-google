from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """
    If it doesn't already exist, returns a Dict and insert it into the instance
    with the file name, number of lines, and content.
    """

    for index in range(len(instance)):
        if path_file in instance.search(index).values():
            return None

    lines = txt_importer(path_file)
    number_of_lines = len(lines)
    process_content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": number_of_lines,
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(process_content)
    print(process_content, file=sys.stdout)


def remove(instance):
    """Removes instace's item if it exists"""

    removed_item = instance.dequeue()

    if not removed_item:
        return print("Não há elementos", file=sys.stdout)

    file_name = removed_item["nome_do_arquivo"]
    print(f"Arquivo {file_name} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
