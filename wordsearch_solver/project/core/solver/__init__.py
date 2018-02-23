from typing import List
from .validators import (Top, TopRight, Right, BottomRight, Bottom, BottomLeft, Left, TopLeft)

class WordSearchSolver:
    def __init__(self, puzzle: List[List[str]], items: List[str]):
        self._puzzle = puzzle
        self._items = items

    def solve(self):
        validators = [
            Top(),
            TopRight(),
            Right(),
            BottomRight(),
            Bottom(),
            BottomLeft(),
            Left(),
            TopLeft()
        ]
        stripped_items = {item.lower().replace(" ", "") for item in self._items}
        solver = _WordSearchSolver(self._puzzle, stripped_items, validators)
        return solver.solve()


class _WordSearchSolver:
    def __init__(self, puzzle: List[List[str]], items: List[str], validators: List[object]):
        self._puzzle = puzzle
        self._items = items
        self._validators = validators
        self._data_info = {
            "rows": len(puzzle),
            "cols": len(puzzle[0])
        }
        self._item_data = {item: len(item) for item in items}

    def solve(self):
        found_items = set()
        found_data = []
        if self._items:
            for row in range(self._data_info["rows"]):
                for col in range(self._data_info["cols"]):
                    diffs = self._items.difference(found_items)
                    if not diffs:
                        return found_data
                    for item in diffs:
                        for validator in self._validators:
                            if validator(self._puzzle,
                                         {"current": row, "len": self._data_info["rows"]},
                                         {"current": col, "len": self._data_info["cols"]},
                                         {"current": item, "len": self._item_data[item]}):
                                found_items.add(item)
                                found_data.append((row, col, item, validator.NAME))
                                break
        return found_data