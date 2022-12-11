from typing import Callable


class Monkey:
    def __init__(self,
                 items: [int],
                 operation: Callable[[int], int],
                 worry_level_modifier: Callable[[int], int],
                 test: Callable[[int], type((int, int))]):
        self._items = items
        self._operation = operation
        self._worry_level_modifier = worry_level_modifier
        self._test = test
        self._inspections = 0

    def __str__(self):
        return ", ".join([str(i) for i in self._items])

    def do_turn(self) -> [(int, int)]:
        actions = []
        for _ in range(len(self._items)):
            self._inspections += 1
            item = self._items.pop()
            actions.insert(0, self._test(self._worry_level_modifier(self._operation(item))))
        return actions

    def get_inspections(self):
        return self._inspections

    def catch_item(self, item: int):
        self._items.insert(0, item)
