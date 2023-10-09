function load_account_info() {
    request_account_info()
}

function request_account_info() {
    let data = JSON_to_obj(http_get("/API?account_info"))
        // console.log(data)
    document.getElementById("email").setAttribute('placeholder', data['email'])
    document.getElementById("secret").setAttribute('placeholder', data['secret'])
    document.getElementById("shared_token").setAttribute('placeholder', data['shared_token'])



    // let form = document.createElement("form");
    // form.id = "account_management"
    // form.setAttribute("method", "post")
    // form.setAttribute("action", "/API?account_setting")

    // Object.keys(data).forEach(
    //     function(key) {
    //         let i = document.createElement("input")
    //         let l = document.createElement("label")
    //         i.setAttribute("type", "text")
    //         i.setAttribute("name", key);
    //         i.id = key
    //         l.setAttribute("for", key)
    //         l.textContent = key + ":"
    //         form.appendChild(l)
    //         form.appendChild(document.createElement("br"))
    //         form.appendChild(i)
    //         form.appendChild(document.createElement("br"))
    //     }
    // );
    // var s = document.createElement("input")
    // s.setAttribute("type", "submit")
    // s.setAttribute("value", "Submit")
    // form.appendChild(s)
    // document.getElementById("info").appendChild(form)
}