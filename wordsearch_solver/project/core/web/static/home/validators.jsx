
class Validator {
    constructor(puzzle, name) {
        this._puzzle = puzzle;
        this._name = name;
    }

    get_name() {
        return this._name;
    }

    check(row_info, col_info, item_info) {
        var cur_row = row_info.current;
        var cur_col = col_info.current;
        var matched = 0;
        var is_valid=false;

        for(var letter_index=0; letter_index < item_info.len; letter_index++) {
            if(this._puzzle[cur_row][cur_col] !== item_info.current[letter_index]) {
                break;
            } else {
                ++matched;
                if(matched === item_info.len) {
                    is_valid=true;
                    break;
                } else {
                    cur_row = this._get_next_row(cur_row, letter_index);
                    cur_col = this._get_next_col(cur_col, letter_index);
                    if(this._should_break({current: cur_row, len: row_info.len}, {current: cur_col, len: col_info.len}))
                        break;
                }
            }
        }
        return is_valid;
    }

    _get_next_row(cur_row, letter_index) {
    }

    _get_next_col(cur_row, letter_index) {

    }

    _should_break(row_info, col_info) {

    }
}


export class Top extends Validator {
    _get_next_col(current_col, current_index) {
        return current_col;
    }

    _get_next_row(current_row, current_index) {
        return current_row - 1;
    }

    _should_break(row_info, col_info) {
        return row_info.current < 0;
    }
}

export class TopRight extends Validator {
    _get_next_col(current_col, current_index) {
         return current_col  + 1
    }

    _get_next_row(current_row, current_index) {
        return current_row - 1
    }

    _should_break(row_info, col_info) {
        return row_info.current < 0 || col_info.current > col_info.len - 1
    }
}

export class Right extends Validator {
    _get_next_col(current_col, current_index) {
         return current_col + 1;
    }

    _get_next_row(current_row, current_index) {
        return current_row;
    }

    _should_break(row_info, col_info) {
        return col_info.current > (col_info.len - 1);
    }
}




export class BottomRight extends Validator {
    _get_next_col(current_col, current_index) {
         return current_col + 1
    }

    _get_next_row(current_row, current_index) {
        return current_row + 1
    }

    _should_break(row_info, col_info) {
        return row_info.current > (row_info.len - 1) || col_info.current > (col_info.len - 1);
    }
}

export class Bottom extends Validator {
    _get_next_col(current_col, current_index) {
         return current_col
    }

    _get_next_row(current_row, current_index) {
        return current_row + 1
    }

    _should_break(row_info, col_info) {
        return row_info.current > (row_info.len - 1)
    }
}




export class BottomLeft extends Validator {
    _get_next_col(current_col, current_index) {
         return current_col - 1
    }

    _get_next_row(current_row, current_index) {
        return current_row + 1
    }

    _should_break(row_info, col_info) {
         return row_info.current > (row_info.len - 1) || col_info.current < 0
    }
}


export class Left extends Validator {
    _get_next_col(current_col, current_index) {
         return current_col - 1
    }

    _get_next_row(current_row, current_index) {
        return current_row;
    }

    _should_break(row_info, col_info) {
         return col_info.current < 0
    }
}

export class TopLeft extends Validator {
    _get_next_col(current_col, current_index) {
         return current_col - 1
    }

    _get_next_row(current_row, current_index) {
        return current_row - 1
    }

    _should_break(row_info, col_info) {
         return row_info.current < 0 ||  col_info.current < 0
    }

}