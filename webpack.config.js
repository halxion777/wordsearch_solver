var webpack = require('webpack');
var path = require("path");
var ExtractTextPlugin = require("extract-text-webpack-plugin");

const config = {
    "entry": {
        "home": path.join(__dirname, "wordsearch_solver", "project", "core", "web", "static", "home", "home.jsx")
    },
    "output": {
        "path": path.join(__dirname, "wordsearch_solver", "project", "core", "web", "static", "dist"),
        "filename": "bundle.js"
    },
    "resolve": {
        "extensions": [".js", ".jsx", ".css"]
    },
    "module": {
        "rules": [
            {
                "test": /\.jsx?/,
                "exclude": "/node_modules/",
                "use": "babel-loader"
            },
            {
                "test": /\.css$/,
                "use": ExtractTextPlugin.extract({
                    "fallback": "style-loader",
                    "use": "css-loader"
                })

            }
        ]
    },
    "plugins": [
        new ExtractTextPlugin("bundle.css")
    ]
};

module.exports = config;
