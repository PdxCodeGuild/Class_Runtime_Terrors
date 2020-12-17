const theHeaders = new Headers()

theHeaders.append('Authorization', 'Token token="83ff6c5e1850ac35856e1869206dd66e"');

let item = document.getElementById('id')
let originator = document.getElementById('author')
let said = document.getElementById('body')

fetch('https://favqs.com/api/quotes?page=1&filter= sex', {
  Method: 'GET',
  headers: theHeaders,
})
  .then(function(response){
    return response.json()
  })
  
  .then(function(data){
    selection = Math.floor(Math.random() * (25-0)) 
    console.log(selection)
    console.log(data)
    number= data.quotes[selection].id
    console.log(number)
    author = data.quotes[selection].author
    console.log(author)
    body = data.quotes[selection].body
    console.log(body)
    item.innerText = `id: ${number}`
    originator.innerText = `author: ${author}`
    said.innerText = `body: ${body}`;

})
  .catch(function(error){
    console.error('There has been a problem with your fetch operation:', error);
  })

  

 
  

