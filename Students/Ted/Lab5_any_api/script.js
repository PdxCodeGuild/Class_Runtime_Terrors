





fetch('https://api.nasa.gov/planetary/apod?api_key=AqXkEe8852lvQ5SgKlAVUJwJ0b0hWoXCwzo3gDPU', {
    Method: 'GET',
    
})
    .then(function(response){
        return response.json()
    })

    .then(function(data){
        console.log(data)
        let image=document.createElement('img');
        image.src= 'data.url'
        console.log(image)
        console.log(data.url)
        let back = document.getElementById('wrapper')
        back.style.backgroundImage=`url(${data.url})`
        // document.body.style.backgroundImage= data.url
        
    })