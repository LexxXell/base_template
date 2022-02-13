const express = require("express");
const Redis = require("ioredis");

const app = express();
const port = process.env.API_PORT ? process.env.API_PORT : 8000;

const redis = new Redis(host = process.env.REDIS_HOST ? process.env.REDIS_HOST : "localhost");

app.get("/api_v1_no/", (req, res) => {
    var _msg = "API.v1 is available";
    var _error = false;
    res.json({ error: _error, message: _msg });
});

app.get("/api_v1_no/check_redis", async(req, res) => {
    try {
        await (async() => {
            const redisInfo = [];
            const _redisInfo = (await redis.info("Server")).split("\r\n");
            [1, 5, 6, 7].forEach(i => redisInfo.push(_redisInfo[i]));
            res.json({ error: false, message: `Redis: ${redisInfo}` });
        })();
    } catch (error) {
        res.json({ error: true, message: "Redis connection error" });
        throw (error);
    }
});

app.listen(port, () => {
    console.log(`The app listening on port ${port}`)
});