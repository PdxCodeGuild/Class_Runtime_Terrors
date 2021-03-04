let req = new XMLHttpRequest();
let qt = "";
let quote = document.getElementById("quote");
let author = document.getElementById("author");
req.overrideMimeType("application/json");
req.open("GET", "https://favqs.com/api/qotd");
req.onload = function () {
    let jsonResponse = JSON.parse(req.responseText);
    console.log(jsonResponse['quote']['author']);
    console.log(jsonResponse['quote']['body']);
    qt = jsonResponse['quote']['body'];
    auth = jsonResponse['quote']['author'];
    quote.innerText = qt;
    author.innerText = "-" + auth;
}
req.send(null);
console.log(qt);