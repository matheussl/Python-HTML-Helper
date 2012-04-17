
"""


This file is part of the Python HTML Helper project


"""

__all__ = [
    'DIV'
]

__scape__ = {
    '<':'&lt;',
    '>':'&gt;',
}

class Tag:
    """
    Generic html tag.
    """

    attr = []
    content = []

    def __init__(self, *args, **kwargs):
        for arg in args:
            self.content.append(arg)
        for kwarg in kwargs:
            self.attr.append(kwarg)

    def __xml__():
        pass

    def __str__():
        pass

    def __getitem__():
        pass

    def __getattr__():
        pass

    def __getcontent__():
        pass






if __name__ == '__main__':
    tag = Tag('a', 'b')
