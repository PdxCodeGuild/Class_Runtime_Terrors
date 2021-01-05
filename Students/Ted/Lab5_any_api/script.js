let marsday= '100'

let i = 0
let time = 3000

fetch(`https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=${marsday}&camera=FHAZ&api_key=mrrK6GWgF16JAzBzCdAmfgMfl4AK6NHz2WYnW3cg`, {
    Method: 'GET',
    
})
    .then(function(response){
        return response.json()

    })

    .then(function(data){
        console.log(data)
        let image=document.createElement('img');
        let shots = data.photos
        image.src= data.photos[0].img_src
        startimage= getElementByTagName('img');
        console.log(image)
        // console.log(data.url)
        let back = document.getElementById('wrapper')
        back.replaceChild(startimage,image)
        // document.body.style.backgroundImage= data.url
        
    })