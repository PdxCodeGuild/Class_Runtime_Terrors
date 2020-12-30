let userData = document.getElementById("user_data")

fetch('https://jsonplaceholder.typicode.com/users')
    .then(function(response){
    return response.json()
    })
    .then(function(data) {
        //use the callback function to display data in the DOM
       console.log(data[0]['name'])
       var users = data
       console.log(users)
       return users
    })


