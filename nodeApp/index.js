const express = require('express');
const app = express();

app.use(express.json());

const port = process.env.PORT || 8080;

app.get("/", (req, res) => {
    res.json("Welcome to the Covid-IoT Project");
});

app.listen(port, () => {
    console.log("Started on Port " + port);
});
