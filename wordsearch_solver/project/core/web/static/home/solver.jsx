import {Top, TopRight, Right, BottomRight, Bottom, BottomLeft, Left, TopLeft} from "./validators";

export class WordSearchGrid {
    constructor(puzzle) {
        this._puzzle = puzzle;

    }


    solve(target_words) {
        var validators = [
            new Top(this._puzzle, "Top"),
            new TopRight(this._puzzle, "TopRight"),
            new Right(this._puzzle, "Right"),
            new BottomRight(this._puzzle, "BottomRight"),
            new Bottom(this._puzzle, "Bottom"),
            new BottomLeft(this._puzzle, "BottomLeft"),
            new Left(this._puzzle, "Left"),
            new TopLeft(this._puzzle, "TopLeft")
        ];

        var scrubbed_targets = target_words.map(function (item) {
            return item.toUpperCase().replace(" ", "");
        })
        var _word_search = new _WordSearchGrid(this._puzzle, scrubbed_targets, validators);
        return _word_search.solve();
    }
}


class _WordSearchGrid {
    constructor(puzzle, target_words, validators) {
        this._puzzle = puzzle;
        this._target_words = target_words;
        this._validators = validators;
        this._data_info = {
            'row': puzzle.length,
            'col': puzzle[0].length
        }
    }


    solve() {
        var found_items = new Set();
        var results = [];
        var validator_length=this._validators.length;
        if(this._target_words.length > 0) {
            var row_index;
            for(row_index = 0; row_index < this._data_info.row; row_index++) {
                var col_index;
                for(col_index = 0; col_index < this._data_info.col; col_index++) {
                    var diff_index;
                    for(diff_index=0; diff_index < this._target_words.length; diff_index++) {
                        for(var validator_index=0; validator_index < validator_length; validator_index++) {
                            var current_validator = this._validators[validator_index];
                            if(current_validator.check({current: row_index, len: this._data_info.row},
                                                       {current: col_index, len: this._data_info.col},
                                                       {current: this._target_words[diff_index], len: this._target_words[diff_index].length})) {
                                // found_items.add(diffs[diff_index]);
                                results.push([row_index, col_index, this._target_words[diff_index], current_validator.get_name()]);
                                // break

                            }
                        }
                    }
                }
            }
        }
        return results;

    }
}