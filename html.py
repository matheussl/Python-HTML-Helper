
"""


This file is part of the Python HTML Helper project


"""


class TAG:
    """
    Generic html tag.
    """
    name = 'tag'
    attr = []
    nodes = []

    def __init__(self, *args, **kwargs):
        for arg in args:
            self.nodes.append(arg)
        for kwarg in kwargs:
            self.attr.append(kwarg)

    def __xml__():
        pass

    def __str__(self):
        result = ['<', self.name, '>']
        nodes = self.__getnodes__()
        for node in nodes:
            result.append('\n    ')
            result.append(node.__str__())
        result.extend(['\n','</', self.name, '>'])
        return ''.join(result)

    def __getitem__(self):
        pass

    def __getattr__(self):
        pass

    def __getnodes__(self):
        return self.nodes






if __name__ == '__main__':
    tag = TAG('a', 'b')
    print tag.__str__()
