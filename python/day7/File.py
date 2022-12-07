class File:
    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size

    def __str__(self):
        return "{} {}".format(self.get_size(), self.get_name())

    def get_size(self):
        return self._size

    def get_name(self):
        return self._name
