console.log('moo');

fetch("http://localhost:8000/todo/api/")
.then(res=> res.json())
.then(data=>console.log(data))