const { Client } = require("pg");

const client = new Client({
    host: process.env.POSTGRES_HOST ? process.env.POSTGRES_HOST : "localhost",
    user: process.env.POSTGRES_USER ? process.env.POSTGRES_USER : "postgres",
    password: process.env.POSTGRES_PASSWORD ? process.env.POSTGRES_PASSWORD : "postgres",
    database: process.env.POSTGRES_DB ? process.env.POSTGRES_DB : "postgres",
    port: 5432
})

client.connect()
client.query('SELECT version()', (err, res) => {
    console.log(err ? "PostgreSQL " + err.message : res.rows[0]["version"]);
    client.end();
});