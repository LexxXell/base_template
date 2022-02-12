const express = require("express");
const app = express();
const port = process.env.API_PORT ? process.env.API_PORT : 8000;

const Pool = require('pg').Pool;

const pool = new Pool({
    host: process.env.POSTGRES_HOST ? process.env.POSTGRES_HOST : "localhost",
    user: process.env.POSTGRES_USER ? process.env.POSTGRES_USER : "postgres",
    password: process.env.POSTGRES_PASSWORD ? process.env.POSTGRES_PASSWORD : "postgres",
    database: process.env.POSTGRES_DB ? process.env.POSTGRES_DB : "postgres",
    port: 5432
})

app.get("/api_v1_no/", (req, res) => {
    var _msg = "API.v1 is available";
    var _error = false;
    res.json({ error: _error, message: _msg });
});

app.get("/api_v1_no/check_postgres", (req, res) => {
    pool.query('SELECT version()', (error, results) => {
        res.json({
            error: error ? true : false,
            message: error ? error : results.rows[0]["version"]
        });
    });
});

app.listen(port, () => {
    console.log(`The app listening on port ${port}`)
});