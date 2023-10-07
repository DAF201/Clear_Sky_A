function load_account_info() {
    request_account_info();
}

function request_account_info() {
    let data = JSON_to_obj(httpGet('/API?account_info'))

    Object.keys(data).forEach(function(key) {
        console.log(key, data[key]);
        let div = document.createElement('div')
        div.id = key;
        div.insertAdjacentElement()
    });
}