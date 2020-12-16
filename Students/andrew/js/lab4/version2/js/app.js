let apiKey = myKey;
let text = {};
console.log(apiKey);

function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token=' + apiKey)
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

const sendReq = (method, url, data) => {
    const promise = new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();

        xhr.open(method, url);
        if (data) {
            xhr.setRequestHeader('Content-Type', 'application/json');
        }
        //xhr.responseType = 'json'; Optional, use in stead of JSON.parse()
        //xhr.response; <- This is now the same data as JSON.parse(xhr.response)

        xhr.onload = () => {
            const data = JSON.parse(xhr.response);// takes the response data and converts it into js
            console.log(data);
        };

        xhr.onerror = () => {
            if (xhr.status >= 400) {
                reject(xhr.response);
            } else {
                resolve(xhr.response);
            }
        };

        xhr.send(JSON.stringify(data));

    });
    return promise;



};


const getData = () => {
    sendReq('GET', 'https://reqres.in/api/users/').then(responseData => {
        console.log(responseData);
    });
};

const sendData = () => {
    sendReq('POST', 'https://reqres.in/api/register', {
        email: "eve.holt@reqres.in",
        password: "pistol"

    }).then(responseData => {
        console.log(responseData);
    }).catch(err => {
        console.log(err);
    });
};



getData();

sendData();
