#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    new_score = max(a_dictionary.values(), default=None)
    for k, v in a_dictionary.items():
        if v == new_score:
            return k
