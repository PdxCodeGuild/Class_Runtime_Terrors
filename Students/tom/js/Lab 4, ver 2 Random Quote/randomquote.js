let key = api()
let quoteSearch = document.getElementById('quoteSearch')
let filterWord = document.getElementById('filterWord')
let page = document.getElementById('page')
const myHeaders = new Headers();

function randonQuote(author, quote) {
    document.getElementById('quote').innerHTML += '<p>' + quote + '&nbsp;&nbsp;&nbsp;&nbsp;-' + author +'</p>'
    // document.getElementById('author').innerHTML = author
    // document.getElementById('quote').innerHTML = quote
}

quoteSearch.addEventListener('click', function(){
    document.getElementById('quote').innerHTML = ''
    let searchText = filterWord.value
    let searchPage = page.value
    let url = `https://favqs.com/api/quotes?page=${searchPage}&filter=${searchText}`

    myHeaders.append('Authorization', `Token token=${key}`);
    console.log(url)
    fetch(url, {
      method: 'GET',
      headers: myHeaders,
    })
     .then(function(response){
        return response.json()
      })
     .then(function(data){
        //or pass a callback function to handle data
        numOfQuotes = data.quotes.length
        console.log(`num of quotes is ${numOfQuotes}`)
        for (i=0; i < data.quotes.length; i++){
            quoteAuthor = data.quotes[i].author
            quoteQuote = data.quotes[i].body
            randonQuote(quoteAuthor, quoteQuote)
        }

    })
      .catch(function(error){
        console.error('There has been a problem with your fetch operation:', error);
      });

})



  function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', `Token token=${key}`)
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        } else if (this.readyState === 4 && this.status === 404) {
            // handle 404
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}