const myHeaders = new Headers();
let key = myKey()
myHeaders.append('Authorization',  `Token token="  ${key} "`);
let x = document.getElementById("btn");
x.addEventListener('click', function() {
  let numInput = document.getElementById('input').values

  fetch("https://favqs.com/api/quotes?page="+numInput,  {
    method: 'GET',
    headers: myHeaders,
  })
  .then(function(response){
      return response.json()
    })
  .then(function(data){
      console.log(data) 
      holDoor = data.quotes 
      document.getElementById("author").innerHTML = holDoor["author"]
      document.getElementById("quote").innerHTML = holDoor["body"]
  })
    .catch(function(error){
      console.error('There has been a problem with your fetch operation:', error);
    })

  })