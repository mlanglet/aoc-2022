from File import File


class Directory:
    def __init__(self, name: str, parent=None):
        if parent is None:
            self._parent = self
        else:
            self._parent = parent

        self._name = name
        self._children = {}

    def __str__(self):
        string = ""
        for key, value in self._children.items():
            if isinstance(value, File):
                string += "{}\n".format(value)
            else:
                string += "dir {}\n".format(value.get_name())
        return string

    def add_child(self, child):
        child.parent = self
        self._children[child.get_name()] = child

    def get_child(self, name):
        return self._children.get(name)

    def get_children(self):
        return self._children

    def get_name(self):
        return self._name

    def get_parent(self):
        return self._parent

    def get_size(self):
        size = 0
        for child in self._children.values():
            size += child.get_size()

        return size
