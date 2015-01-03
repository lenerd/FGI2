from itertools import chain, combinations


class Place:
    def __init__(self, name, get, put):
        self.name = name
        self.get = get
        self.put = put

    def __str__(self):
        return self.name

    __repr__ = __str__


P = [
    Place('p1', {'b', 'e'}, {'a', 'c'}),
    Place('p2', {'b'}, {'a', 'd', 'e'}),
    Place('p3', {'d'}, {'b', 'c'}),
    Place('p4', {'c', 'd', 'e'}, {'d'}),
    Place('p5', {'a'}, {'d', 'e'}),
]


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def main():
    power = powerset(P)
    traps = set()
    siphons = set()
    for p in power:
        put = set()
        get = set()
        for pl in p:
            put = put.union(pl.put)
            get = get.union(pl.get)
        if get.issubset(put):
            print("trap:\t{}".format(p))
            traps.add(p)
        if get.issuperset(put):
            print("siphon:\t{}".format(p))
            siphons.add(p)
    print("{} traps".format(len(traps)))
    print("{} siphons".format(len(siphons)))


if __name__ == '__main__':
    main()
