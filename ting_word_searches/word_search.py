def get_word_occurrences(lines, word, simplified):
    """
    Recives an list of string and returns a list of dicts
    with all occurrences or None
    """

    occurrences = list()

    for index in range(len(lines)):
        if word.lower() in lines[index].lower():
            if simplified:
                occurrences.append({"linha": index + 1})
            else:
                occurrences.append({
                    "linha": index + 1, "conteudo": lines[index]})

    if not occurrences:
        return None

    return occurrences


def handle_results(word, instance, simplified):
    """
    Properly formats information about the number of occurrences of a word
    """

    if not word or not isinstance(word, str):
        return []

    results = list()

    for index in range(len(instance)):
        lines = instance.search(index)["linhas_do_arquivo"]
        occurrences = get_word_occurrences(lines, word, simplified)

        if occurrences:
            results.append({
                "arquivo": instance.search(index)["nome_do_arquivo"],
                "ocorrencias": occurrences,
                "palavra": word,
            })

    return results


def exists_word(word, instance):
    """
    Returns simplified information about every time a word appears
    in one value of the instance
    """
    return handle_results(word, instance, True)


def search_by_word(word, instance):
    """
    Returns information about every time a word appears
    in one value of the instance
    """
    return handle_results(word, instance, False)
