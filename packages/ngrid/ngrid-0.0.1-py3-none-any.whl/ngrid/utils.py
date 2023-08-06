from math import floor


def reduce_periodic(a, b, x):
    return x - floor((x-a)/(b-a)) * (b-a)
