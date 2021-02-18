function dakine(){
    let kaneohe = 'kaneohe'
    // if (icon.hasChildNodes){
    //     icon.innerText = '';
    // }
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${kaneohe}&appid=8af2aa7fa978da0c3dc608a85406875c`)
//   method: 'GET',
//   headers: myHeaders,
// })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        console.log(data) 
        console.log(data.wind.speed)
        console.log(data.wind.deg)
        let speed = document.getElementById('kaneohe_wind_speed')
        speed.innerText = data.wind.speed;
        //if you want to change to cardinal dir thats cool
        let direction = document.getElementById('kaneohe_wind_direction')
        direction.innerText = data.wind.deg;
    })
    .catch(function(error){
        console.error('There has been a problem with your fetch operation:', error);
    });
}
    

function aiea(){
        let aiea = 'aiea'
        // if (icon.hasChildNodes){
        //     icon.innerText = '';
        // }
        fetch(`https://api.openweathermap.org/data/2.5/weather?q=${aiea}&appid=8af2aa7fa978da0c3dc608a85406875c`)
    //   method: 'GET',
    //   headers: myHeaders,
    // })
        .then(function(response){
            return response.json()
        })
        .then(function(data){
            console.log(data) 
            console.log(data.wind.speed)
            console.log(data.wind.deg)
            let speed = document.getElementById('hickam_wind_speed')
            speed.innerText = data.wind.speed;
            //if you want to change to cardinal dir thats cool
            let direction = document.getElementById('hickam_wind_direction')
            direction.innerText = data.wind.deg;
        })
        .catch(function(error){
            console.error('There has been a problem with your fetch operation:', error);
        });
        }
dakine()
aiea()