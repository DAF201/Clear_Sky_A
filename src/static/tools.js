function print(obj, alarm = false) {
    console.log(obj)
    if (alarm) {
        window.alarm(obj)
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function replace(url, delay = 0, method = "get") {
    await sleep(delay)
    if (method == "get") {
        window.location.replace(url)
    } else if (method == "post") {
        var form = document.createElement("form");
        document.body.appendChild(form);
        form.method = "post";
        form.action = url;
        form.submit();
    }
}

function http_get(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function JSON_to_obj(str) {
    return JSON.parse(str)
}