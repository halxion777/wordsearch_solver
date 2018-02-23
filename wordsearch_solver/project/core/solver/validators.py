from typing import Dict, Union


class Direction:
    NAME = ""

    def __call__(self, *args, **kwargs):
        return self._check(*args, **kwargs)

    def _check(self,
               puzzle,
               row_info: Dict[str, int],
               col_info: Dict[str, int],
               item_info: Dict[str, Union[str, int]]) -> bool:
        cur_row = row_info["current"]
        cur_col = col_info["current"]
        letters_matched = 0
        is_valid = False
        for index, letter in enumerate(item_info["current"]):
            if puzzle[cur_row][cur_col] != letter:
                break
            else:
                letters_matched += 1
                if letters_matched == item_info["len"]:
                    is_valid = True
                    break
                cur_row = self._get_next_row(cur_row, index)
                cur_col = self._get_next_col(cur_col, index)
                if self._should_break({'current': cur_row, "len": row_info["len"]},
                                      {"current": cur_col, "len": col_info["len"]}):
                    break
        return is_valid

    def _get_next_row(self, current_row: int, current_index: int) -> int:
        pass

    def _get_next_col(self, current_col: int, current_index: int) -> int:
        pass

    def _should_break(self, row_info: Dict[str, int], col_info: Dict[str, int]) -> bool:
        pass


class Top(Direction):
    NAME = "Top"

    def _get_next_col(self, current_col: int, current_index: int) -> int:
        return current_col

    def _get_next_row(self, current_row: int, current_index: int) -> int:
        return current_row - 1

    def _should_break(self, row_info: Dict[str, int], col_info: Dict[str, int]) -> bool:
        return row_info["current"] < 0


class TopRight(Direction):
    NAME = "Top Right"

    def _get_next_col(self, current_col: int, current_index: int):
        return current_col  + 1

    def _get_next_row(self, current_row: int, current_index: int):
        return current_row - 1

    def _should_break(self, row_info: Dict[str, int], col_info: Dict[str, int]):
        return row_info["current"] < 0 or col_info["current"] > col_info["len"] - 1


class Right(Direction):
    NAME = "Right"

    def _get_next_col(self, current_col: int, current_index: int) -> int:
        return current_col + 1

    def _get_next_row(self, current_row: int, current_index: int):
        return current_row

    def _should_break(self, row_info: Dict[str, int], col_info: Dict[str, int]):
        return col_info["current"] > (col_info["len"] - 1)


class BottomRight(Direction):
    NAME = "Bottom Right"

    def _get_next_col(self, current_col: int, current_index: int) -> int:
        return current_col + 1

    def _get_next_row(self, current_row: int, current_index: int) -> int:
        return current_row + 1

    def _should_break(self, row_info: Dict[str, int], col_info: Dict[str, int]):
        return row_info["current"] > (row_info["len"] - 1) or col_info["current"] > (col_info["len"] - 1)


class Bottom(Direction):
    NAME = "Bottom"

    def _get_next_row(self, current_row: int, current_index: int) -> int:
        return current_row + 1

    def _get_next_col(self, current_col: int, current_index: int) -> int:
        return current_col

    def _should_break(self, row_info: Dict[str, int], col_info: Dict[str, int]):
        return row_info["current"] > (row_info["len"] - 1)


class BottomLeft(Direction):
    NAME = "Bottom Left"

    def _get_next_row(self, current_row: int, current_index: int) -> int:
        return current_row + 1

    def _get_next_col(self, current_col: int, current_index: int) -> int:
        return current_col - 1

    def _should_break(self, row_info: Dict[str, int], col_info: Dict[str, int]) -> bool:
        return row_info["current"] > (row_info["len"] - 1) or col_info["current"] < 0


class Left(Direction):
    NAME = "Left"

    def _get_next_row(self, current_row: int, current_index: int) -> int:
        return current_row

    def _get_next_col(self, current_col: int, current_index: int) -> int:
        return current_col - 1

    def _should_break(self, row_info: Dict[str, int], col_info: Dict[str, int]):
        return col_info["current"] < 0


class TopLeft(Direction):
    NAME = "Top Left"

    def _get_next_row(self, current_row: int, current_index: int) -> int:
        return current_row - 1

    def _get_next_col(self, current_col: int, current_index: int) -> int:
        return current_col - 1

    def _should_break(self, row_info: Dict[str, int], col_info: Dict[str, int]) -> bool:
        return row_info["current"] < 0 or col_info["current"] < 0