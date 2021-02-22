fetch("http://localhost8000/todo/api/")
.then(res=> res.json)
.then(data=>console.log(data))
console.log("Bill Murray was here, and nobody will believe you...")