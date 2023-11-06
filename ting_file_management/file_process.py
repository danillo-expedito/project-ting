import sys
from .file_management import txt_importer


def process(path_file, instance):
    file_list = txt_importer(path_file)
    for i in range(len(instance.queue)):
        if instance.queue[i]["nome_do_arquivo"] == path_file:
            return None

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_list),
        "linhas_do_arquivo": file_list,
    }
    instance.enqueue(new_dict)
    sys.stdout.write(str(new_dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
