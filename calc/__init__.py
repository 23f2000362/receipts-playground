def add(a, b):
    return a + b


def clamp(x, lo, hi):
    return max(lo, min(x, hi))


def slow():
    from fancyretry import backoff
    return backoff
