console.log('moo');

fetch("http://localhost:8000/api-data/")
.then(res=> res.json())
.then(data=>console.log(data))