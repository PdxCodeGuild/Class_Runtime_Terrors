let apiKey = myKey;

console.log(apiKey);

const quotesArray = (data) => {
    for (let i = 0; i < 5; i++) {

        console.log(data['quotes'][i]['author']);
        console.log(data['quotes'][i]['body']);
        if (data['quotes'][i]['tags'][0] === undefined) {
            //set innerText to something else
            console.log("NO TAG")
        } else {
            console.log(data['quotes'][i]['tags'][0]);
        }


    }
    return data;
};


const cardArray = (qt) => {
    
    for (let i = 0; i < 5; i++) {
        const bod = document.getElementById('body');
        const cardMain = document.createElement('div');
        cardMain.setAttribute('class', 'card');
        cardMain.setAttribute('style', 'width: 18rem');

        const cardBody = document.createElement('div');
        cardBody.setAttribute('class', 'card-body');
        cardBody.setAttribute('id', i);

        let card = document.getElementsByClassName('card');
        let authorNode = document.createTextNode("Author");
        let quoteNode = document.createTextNode('quote')
        let tagNode = document.createTextNode('Tag');

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
            quotesArry(data);



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







