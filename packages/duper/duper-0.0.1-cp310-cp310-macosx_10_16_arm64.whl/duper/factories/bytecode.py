"""
Generating AST only to dump it to bytecode is slow and wasteful
pickle and marshal can be ~50x faster on initial dump,
I believe that's because they're generating bytecode without generating AST

>>> import duper, marshal, pickle
>>> x = {"a": 1, "b": [(1, 2, 3), (4, 5, 6)], "c": []}
>>> reconstructor = duper.dup(x)   # ~0.00002941 ms (duper_compile)
>>> marshal_dumped = marshal.dumps(x)  # ~0.00000045 ms (marshal_dumps): 65.52 times faster than duper_compile
>>> pickle_dumped = pickle.dumps(x)    # ~0.00000055 ms (pickle_dumps): 53.81 times faster than duper_compile

But generating bytecode is harder since there's not much examples of doing that by hand
However, I assume it will be much easier to build bytecode factories
by copying AST factories once they are in their _final_ implementation

https://stackoverflow.com/questions/75001222/convert-python-code-to-byte-code-to-binary-and-print-out-the-binary-in-a-list
"""
raise NotImplementedError(
    "bytecode factories are not implemented yet, but should be:\n" + globals()["__doc__"]
)
