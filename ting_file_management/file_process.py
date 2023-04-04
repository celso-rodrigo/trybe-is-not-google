from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
