let marsday= '1'


fetch(`https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=${marsday}&camera=NAVCAM&api_key=mrrK6GWgF16JAzBzCdAmfgMfl4AK6NHz2WYnW3cg`, {
    Method: 'GET',
    
})
    .then(function(response){
        return response.json()

    })

    .then(function(data){
        console.log(data)
        let image=document.createElement('img');
        // let i = 0;
        // while (i < Array.length){

        // }
        image.src= data.photos[3].img_src

        console.log(image)
        // console.log(data.url)
        let back = document.getElementById('wrapper')
        back.appendChild(image)
        // document.body.style.backgroundImage= data.url
        
    })