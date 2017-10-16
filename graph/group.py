from string import ascii_lowercase

class Group:
    def __init__(self, elements, operator, namingStrategy = None):
        self.elements = elements
        self.operator = operator
        self.nameToElement = {}
        self.elementToName = {}
        names = ascii_lowercase if namingStrategy == None else map(namingStrategy, elements)
        for element, name in zip(elements, names):
            self.elementToName[element] = name
            self.nameToElement[name] = element

    def operate(self, a, b):
        return self.operator(a, b)

    def getElements(self):
        return self.elements

    def getTable(self):
        lines = []
        header = list(self.nameToElement.keys())
        header.insert(0, ' ')
        lines.append(header)
        for n_a, a in self.nameToElement.iteritems():
            line = [n_a]
            for n_b, b in self.nameToElement.iteritems():
                line.append(self.elementToName[self.operator(a, b)])
            lines.append(line)
        return lines
