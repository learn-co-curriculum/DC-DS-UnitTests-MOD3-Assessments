def flatten(l):
    if isinstance(l, (list, tuple)):
        return flatten(l[0])
    return l