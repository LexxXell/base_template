const express = require("express");
const app = express();
const port = process.env.API_PORT ? process.env.API_PORT : 8000;

app.get("/api_v1_no/", (req, res) => {
    var _msg = "API.v1 is available";
    var _error = false;
    res.json({ error: _error, message: _msg });
});

app.listen(port, () => {
    console.log(`The app listening on port ${port}`)
});