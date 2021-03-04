let apiKey = myKey;

console.log(apiKey);
let card = document.getElementsByClassName('card');



const cardArray = (quotes) => {
    let qt = quotes;

    let tag =""
    for (let i = 0; i < 5; i++) {
        let author = qt['quotes'][i]['author'];
        let body = qt['quotes'][i]['body'];

        if ( qt['quotes'][i]['tags'][0] === undefined){
            tag = "NO TAG";
        }else{
            tag = qt['quotes'][i]['tags'];
        }

        const bod = document.getElementById('qtbod');
        const cardMain = document.createElement('div');
        cardMain.setAttribute('class', 'card');
        cardMain.setAttribute('style', 'width: 18rem');

        const cardBody = document.createElement('div');
        cardBody.setAttribute('class', 'card-body');
        cardBody.setAttribute('id', i);

        
        let authorNode = document.createTextNode("Author -" +author);
        
        let quoteNode = document.createTextNode(body);
        let tagNode = document.createTextNode("Tag: "+ tag);

        let authDiv = document.createElement('div');
        let quoteDiv = document.createElement('div');
        let tagDiv = document.createElement('div');

        authDiv.setAttribute('id', i);
        quoteDiv.setAttribute('id', i);
        tagDiv.setAttribute('id', i);

        cardBody.appendChild(quoteDiv);
        cardBody.appendChild(authDiv);
        cardBody.appendChild(tagDiv);

        bod.appendChild(cardMain);
        cardMain.appendChild(cardBody);
        quoteDiv.appendChild(quoteNode);
        authDiv.appendChild(authorNode);
        cardBody.appendChild(tagNode);
        
    }
    
};



const sendReq = (method, url, data) => {
    const promise = new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();

        xhr.open(method, url);

        xhr.setRequestHeader("Authorization", "Token token=" + apiKey.KEY);

        //xhr.responseType = 'json'; Optional, use in stead of JSON.parse()
        //xhr.response; <- This is now the same data as JSON.parse(xhr.response)

        xhr.onload = () => {
            const data = JSON.parse(xhr.response); // takes the response data and converts it into js
            cardArray(data);

        };

        xhr.onerror = () => {
            if (xhr.status >= 400) {
                reject(xhr.response);
            } else {
                resolve(xhr.response);
            }
        };

        xhr.send();

    });
    return promise;

};


const getData = () => {
    sendReq('GET', 'https://favqs.com/api/quotes').then(responseData => {
    });
};


let fetchQuotes = [];
function sendFetchReq(){
    let init = {headers: {"Authorization": "Token token=" + apiKey.KEY}};
    fetch('https://favqs.com/api/quotes',init)
    .then(response => response.json())
    .then(showData => cardArray(showData));

    
}




