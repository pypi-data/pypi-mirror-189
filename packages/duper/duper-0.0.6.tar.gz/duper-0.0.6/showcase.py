import copy

import duper
from timesup import timesup


@timesup(number=10000, repeats=3)
def reconstruction():
    x = {"a": 1, "b": [(1, 2, 3), (4, 5, 6)], "c": [object(), object(), object()]}  # i

    # prepare constructor beforehand
    dup = duper.Duper(x, prepare=True)  # t duper_init
    copy.deepcopy(x)  # t deepcopy
    dup.deep()  # t duper_reconstruct deepcopy
