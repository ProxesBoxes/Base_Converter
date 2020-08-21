
def is_list_of_strings(lst):
    return bool(lst) and isinstance(lst, list) and all(isinstance(elem, str) for elem in lst)
