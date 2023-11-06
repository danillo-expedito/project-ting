def find_word(word, instance, show_content=False):
    word = word.lower()
    result = []

    for item in instance.queue:
        file_name = item["nome_do_arquivo"]
        lines = item["linhas_do_arquivo"]
        occurrences = []

        for line_number, line in enumerate(lines, start=1):
            if word in line.lower():
                occ = {"linha": line_number}
                if show_content:
                    occ["conteudo"] = line
                occurrences.append(occ)

        body = {
            "arquivo": file_name,
            "ocorrencias": occurrences,
            "palavra": word,
        }
        result.append(body)

    return result


def exists_word(word, instance):
    result = find_word(word, instance)
    return result if result[0]["ocorrencias"] else []


def search_by_word(word, instance):
    result = find_word(word, instance, show_content=True)
    return result if result[0]["ocorrencias"] else []
