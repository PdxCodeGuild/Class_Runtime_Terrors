let apiKey = myKey.KEY;
let text = {};
console.log(apiKey);

function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token='+ apiKey)
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        } else if (this.readyState === 4 && this.status === 404) {
            //Alert user to a 404 exception
            alert("404 error!")
        }

        console.log()
    };
    xhttp.open("GET", url);
    xhttp.send();
}

http_get('https://favqs.com/api/',text)