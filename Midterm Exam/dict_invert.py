def dict_invert(d):
    """
    Takes in a dictionary with immutable values and returns the inverse of the
    dictionary.
    The inverse of a dictionary d is another dictionary whose keys are the
    unique dictionary values in d.
    The value of a key in the inverse dictionary is a ascending sorted list of
    all keys in d that have the same value in d.
    Arguments:
        d: A dictionary with immutable values
    Returns an inverted dictionary according to the instructions above.
    """

    invert_d = {}
    for value in d.values():
        invert_d[value] = invert_d.get(value, [])

    for key in d.keys():
        invert_d[d[key]].append(key)

    for key in invert_d.keys():
        invert_d[key].sort()

    return invert_d
