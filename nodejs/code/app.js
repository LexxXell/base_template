const Redis = require("ioredis");

const redis = new Redis(host = process.env.REDIS_HOST ? process.env.REDIS_HOST : "localhost");

async function getRedisInfo() {
    const redisInfo = [];
    const _redisInfo = (await redis.info("Server")).split("\r\n");
    [1, 5, 6, 7].forEach(i => redisInfo.push(_redisInfo[i]));
    return `Redis: ${redisInfo.join(", ")}`;
}

(async() => {
    console.log(await getRedisInfo());
})();