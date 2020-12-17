let item = document.getElementById('id')
let originator = document.getElementById('author')
let said = document.getElementById('body')

fetch('https://favqs.com/api/qotd')
  .then(response => response.json())
  .then(data => {
    console.log(data)
    number= data.quote.id
    console.log(number)
    author = data.quote.author
    console.log(author)
    body = data.quote.body
    console.log(body)
    item.innerText = `id: ${number}`
    originator.innerText = `author: ${author}`
    said.innerText = `body: ${body}`;

  })
  
// console.log(number, this.number);
 
  

