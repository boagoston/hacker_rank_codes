def permitido(s):
    if not s:
        return False
    return len(s) == len(set(s))


