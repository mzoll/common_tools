import math

def gen_n_chunks(obj, n):
    """ return n junks of this object as a generator """
    batchsize = math.ceil(len(obj) / n)
    s = 0
    e = s + batchsize
    while e < len(obj):
        yield obj[s:e]
        s = e
        e = min(e + batchsize, len(obj))
    yield obj[s:]

def gen_maxsize_chunks(obj, maxsize):
    """ return junks no bigger than maxsize of this object as a generator """
    for i in range(math.ceil(len(obj) / maxsize)):
        yield obj[i * maxsize: min(len(obj), (i + 1) * maxsize - 1)]
