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
    sys.stdout.write(str(new_dict) + "\n")


def remove(instance):
    if len(instance.queue) == 0:
        sys.stdout.write("Não há elementos\n")
        return None

    removed_item = instance.dequeue()
    sys.stdout.write(
        f"Arquivo {removed_item['nome_do_arquivo']} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
