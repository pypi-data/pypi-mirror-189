import itertools
import sys

it = sys.modules[__name__]


def bol(*args):
    condi = args[-1]
    i = args[:-1]
    for p in itertools.product(*i):
        if condi():
            return
        yield p
