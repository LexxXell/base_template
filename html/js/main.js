const baseApiURL = {
    node: "/api_v1_no/",
    python: "/api_v1_py/"
}
const checkPostgres = "check_postgres";
const checkRedis = "check_redis";

function setApiCheckResults(baseURL, apiInfoObj, postgresInfoObj, redisInfoObj) {
    const apiData = httpGetJSON(baseURL);
    const postgresData = httpGetJSON(baseURL + checkPostgres);
    const redisData = httpGetJSON(baseURL + checkRedis);
    apiInfoObj.textContent = apiData.message ? apiData.message : apiInfoObj.textContent;
    apiInfoObj.className = apiData.error ? "i_t__p_e" : "i_t__p_s";
    postgresInfoObj.textContent = postgresData.message ? postgresData.message : postgresInfoObj.textContent;
    postgresInfoObj.className = postgresData.error ? "i_t__p_e" : "i_t__p_s";
    redisInfoObj.textContent = redisData.message ? redisData.message : redisInfoObj.textContent;
    redisInfoObj.className = redisData.error ? "i_t__p_e" : "i_t__p_s";
}

function httpGetJSON(theUrl) {
    try {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open("GET", theUrl, false); // false for synchronous request
        xmlHttp.send(null);
        return JSON.parse(xmlHttp.responseText);
    } catch {
        return { error: true }
    }
}

setApiCheckResults(
    baseURL = baseApiURL["python"],
    apiInfoObj = document.querySelector('#api_py_info'),
    postgresInfoObj = document.querySelector('#postgres_py_info'),
    redisInfoObj = document.querySelector('#redis_py_info')
)

setApiCheckResults(
    baseURL = baseApiURL["node"],
    apiInfoObj = document.querySelector('#api_no_info'),
    postgresInfoObj = document.querySelector('#postgres_no_info'),
    redisInfoObj = document.querySelector('#redis_no_info')
)