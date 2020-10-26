const express = require('express');
const app = express();

app.use(express.json());

const port = process.env.PORT || 8080;

app.get("/", (req, res) => {
    res.json("Welcome to the Covid-IoT Project");
});

app.get("/charts", (req, res) => {
    var options = {
        root: __dirname,
        dotfiles: 'deny',
    }
    res.sendFile('charts.html', options, function(err) {});
});

app.get("/data", (req, res) => {
    var options = {
        root: __dirname,
        dotfiles: 'deny',
    }
    res.sendFile('table.html', options, function(err) {});
})

app.listen(port, () => {
    console.log("Started on Port " + port);
});