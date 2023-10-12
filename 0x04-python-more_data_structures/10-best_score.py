#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    makey = list(a_dictionary.keys())[0]

    for key in a_dictionary.keys():
        if a_dictionary[makey] < a_dictionary[key]:
            makey = key
    return makey
