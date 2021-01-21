const myHeaders = new Headers();

myHeaders.append('Authorization',  'Token token=""');

fetch('https://favqs.com/api/qotd', {
  method: 'GET',
  headers: myHeaders,
})
 .then(function(response){
    return response.json()
  })
 .then(function(data){
    let getQuote = document.getElementById('api_get')
    var author = data.quote.author
    var body = data.quote.body
    getQuote.innerHTML = body\ + " " + author
    console.log(author) 
    console.log(body)
    
    
})
  .catch(function(error){
    console.error('There has been a problem with your fetch operation:', error);
  });

let getQuote = document.getElementById('api_get')
getQuote.style.backgroundColor = 'black'
getQuote.style.color = 'white'

