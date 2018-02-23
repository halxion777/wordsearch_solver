import React from "react";
import ReactDOM from "react-dom";
import {WordSearchGrid} from "./solver";
import Select from 'react-select';
import 'react-select/dist/react-select.css';


require("./home.css");
var axios = require("axios");
// var $ = require("jquery");

class GridPuzzle extends React.Component{
    constructor(props) {
        super(props)
        this.state = {
            puzzle: [],
            used_colors: null,
            row_size: 0,
            col_size: 0,
            actives: {},
            word_count: 0,
            current_targets: [],
            added_targets: {},
            current_search_color: $.xcolor.random(),
            sample_file: null,
            sample_files: [
                {label: "Arguments", value: "arguments_data"},
                {label: "European Countries", value: "european_countries"},
                {label: "Lots of Words", value: "lots_of_words"},
                {label: "US States", value: "us_states"}

            ]
        }

    }

     read_json_file(event) {
        var _this = this;
        var reader = new FileReader();
        reader.onload = function (event) {
            var parsed = JSON.parse(event.target.result).data;
            _this.setState({
                puzzle: parsed,
                row_size: parsed.length,
                col_size: parsed[0].length
            });

            _this.solver = new WordSearchGrid(parsed);
        }

        reader.readAsText(event.target.files[0])
    }

    highlight_coord(row, col, word_len, direction) {
        var coord_index;
        switch(direction) {
            case "Left":
                var col=col;
                var state = this.state.puzzle;
                var coords = []
                for(col; word_len > 0; word_len--, col--) {
                    coords.push(row.toString() + "," + col.toString())
                }
                return coords;
            case "Right":
                var col=col;
                var state = this.state.puzzle;
                var coords = []
                for(col; word_len > 0; word_len--, col++) {
                    coords.push(row.toString() + "," + col.toString())
                }
                return coords;
            case "Top":
                var row=row;
                var coords = []
                for(row; word_len > 0; word_len--, row--) {
                    coords.push(row.toString() + "," + col.toString())
                }
                return coords;
            case "Bottom":
                var row=row;
                var coords = [];
                for(row; word_len > 0; word_len--, row++) {
                    coords.push(row.toString() + "," + col.toString())
                }
                return coords;
            case "BottomRight":
                var row=row;
                var col=col;
                var coords = [];
                for(row; word_len > 0; word_len--, row++, col++) {
                    coords.push(row.toString() + "," + col.toString())
                }
                return coords;

            case "BottomLeft":
                var row=row;
                var col=col;
                var coords = [];
                for(row; word_len > 0; word_len--, row++, col--) {
                    coords.push(row.toString() + "," + col.toString())
                }
                return coords;

            case "TopLeft":
            var row=row;
            var col=col;
            var coords = [];
            for(row; word_len > 0; word_len--, row--, col--) {
                coords.push(row.toString() + "," + col.toString())
            }
            return coords;

           case "TopRight":
                var row=row;
                var col=col;
                var coords = [];
                for(row; word_len > 0; word_len--, row--, col++) {
                    coords.push(row.toString() + "," + col.toString())
                }
                return coords;
        }

    }

    search_word(event) {
        var word = this.refs.word_search.value.toUpperCase().replace(/ /g, "");
        var current_actives = {};
        var coords = this.solver.solve([word]);
        var index;
        var state = this.state;

        for(index=0; index < coords.length; index++) {
            var current_coords = coords[index];
            var highlighted = this.highlight_coord(current_coords[0], current_coords[1], current_coords[2].length, current_coords[3]);

            if(highlighted !== undefined) {
                 highlighted.forEach(function (item) {
                current_actives[item] = {is_active: true, color: state.current_search_color, word: current_coords[2]};
                 })
            }
        }
        this.setState({actives: current_actives, word_count: coords.length});






    }

    create_grid() {
        var grid = [];
        var current_active = this.state.actives;
        var target_active = this.state.added_targets;
        var should_update = false;
        for(var row=0; row < this.state.row_size; row++) {
            var cols = [];
            for(var col=0; col < this.state.col_size; col++) {
                var current_item = this.state.puzzle[row][col];
                var cell_id = row.toString() + "," + col.toString()
                var selected = current_active[cell_id];
                var is_active=false;
                var background=null;
                Object.keys(target_active).forEach(function (item) {
                     if(target_active[item].active_areas[cell_id] !== undefined) {
                         background = target_active[item].active_areas[cell_id].color;
                     }
                 });

                if(selected !== undefined) {

                    is_active = selected.is_active;
                    if(background !== null) {
                         background = $.xcolor.average(background, current_active[cell_id].color);
                         current_active[cell_id].color = background
                         should_update=true
                    }
                    else
                        background=current_active[row.toString() + "," + col.toString()].color;
                }



                cols.push(<div  style={{backgroundColor: background}} className={["ws_cell", is_active? "active_cell": ""].join(" ")}>{current_item.toUpperCase()}</div>)
            }
            grid.push(<div className={"ws_row"}>{cols}</div>);
        }
        return grid;
    }

    handle_input(event) {
        var enter_pressed = event.type === "keydown" && event.key === "Enter";
        var clicked = event.type === "click";
        if(enter_pressed || clicked)
            this.add_target();
    }

    add_target() {

        var state = this.state;
        var input_value = this.refs.word_search.value.replace(/ /g, "").toUpperCase();
        if(input_value.length > 0) {
            var should_add = false;
            for (var index = 0; index < state.current_targets.length; index++) {
                if (state.current_targets[index].key === input_value) {
                    should_add = true;
                    break;
                }
            }
            if (should_add) {
                this.refs.word_search.value = '';
                var current_search_color = state.current_search_color;
                var new_color = $.xcolor.random();
                while (state.used_colors.has(new_color)) {
                    new_color = $.xcolor.random()
                }
                state.used_colors.add(current_search_color);
                state.current_search_color = new_color;

                state.added_targets[input_value] = {
                    active_areas: this.state.actives,
                    color: current_search_color,
                    count: state.word_count
                }
                this.setState(state);
            }
        }
    }

    get_samplefiles(new_val) {
        var _this = this;
        axios.get("/api/sample_data?file_name=" + new_val.value).then(function (resp) {
            var data = resp.data.data;
            var scrubbed_target_words = resp.data.target_words.map(function (item) {
                var obj = {key: item.replace(/ /g, "").toUpperCase(), value: item};
                return obj;

            });

            _this.setState({
                puzzle: data,
                row_size: data.length,
                col_size: data[0].length,
                sample_file: new_val,
                current_targets: scrubbed_target_words,
                added_targets: {},
                actives: {},
                used_colors: new Set(),


            });
            _this.refs.word_search.value = '';
            _this.solver = new WordSearchGrid(data);
        })

    }

    get_current_targets() {
        var current_targets = this.state.current_targets.map(function (item) {
            return item.value;
        });
        var _this = this;
        var items = current_targets.map(function (item) {
            var item_id = item.replace(/ /g, "").toUpperCase();
            var added_target = _this.state.added_targets[item_id];
            var is_added = added_target !== undefined;
            return <div id={item_id} style={{backgroundColor: is_added ? added_target.color: null}} className={"current_targets"}>{item}</div>
        })
        return items;
    }


    render() {
        return (
            <div id={"puzzle_page"}>
                <div id={"puzzle_area"}>{this.create_grid()}</div>
                <div id={"misc"}>
                    <Select value={this.state.sample_file} options={this.state.sample_files} onChange={this.get_samplefiles.bind(this)} />
                    <input id={"upload"} type={"file"} onChange={this.read_json_file.bind(this)} accept=".json"/>
                    <input onKeyDown={this.handle_input.bind(this)} id={"word_search"} ref={"word_search"} onChange={this.search_word.bind(this)}/>
                    <button onClick={this.handle_input.bind(this)} id={"add_searched"}>Mark</button>
                </div>
                <div id={"word_targets"}>
                    {this.get_current_targets()}
                </div>
            </div>
        )
    }

}


class HomeComponent extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            puzzle: [],
            row: 0,
            col: 0
        }

        this.solver = null;
    }


    render() {
        return (
            <div>
                <GridPuzzle/>
            </div>

        )
    }

}


ReactDOM.render(<HomeComponent/>, document.getElementById("main_body"));








