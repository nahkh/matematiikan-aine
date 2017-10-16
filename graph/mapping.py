class Mapping:
    def __init__(self, original, permuted):
        self.original = original
        self.permuted = tuple(permuted)
        self.forward = {}
        for a, b in zip(original, permuted):
            self.forward[a] = b

    def __getitem__(self, arg):
        return self.forward[arg]

    def __call__(self, arg):
        return self[arg]

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.permuted == other.permuted
        return False

    def __hash__(self):
        return hash(self.permuted)

    def reverse(self):
        newMapping = Mapping([], [])
        newMapping.forward = dict([[v,k] for k,v in self.forward.items()])
        return newMapping

    def merge(self, b):
        '''Equivalent to f o b'''
        permuted = []
        for original in self.original:
            permuted.append(self.forward[b[original]])
        return Mapping(self.original, permuted)
