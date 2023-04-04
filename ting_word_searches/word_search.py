def get_word_occurrences(lines, word):
    """
    Recives an list of string and returns a list of dicts
    with all occurrences or None
    """

    occurrences = list()

    for index in range(len(lines)):
        if word.lower() in lines[index].lower():
            occurrences.append({"linha": index + 1})

    if len(occurrences) == 0:
        return None

    return occurrences


def exists_word(word, instance):
    """
    Returns information about every time a word appears
    in one value of the instance
    """

    if not word or not isinstance(word, str):
        return []

    results = list()

    for index_data in range(len(instance)):
        lines = instance.search(index_data)["linhas_do_arquivo"]
        occurrences = get_word_occurrences(lines, word)

        if occurrences:
            results.append({
                "arquivo": instance.search(index_data)["nome_do_arquivo"],
                "ocorrencias": occurrences,
                "palavra": word,
            })

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
