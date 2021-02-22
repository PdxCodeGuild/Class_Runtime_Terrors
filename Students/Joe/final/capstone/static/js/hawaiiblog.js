var mymap = L.map('mapid').setView([51.505, -0.09], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'your.mapbox.access.token'
}).addTo(mymap);

function myFunction(){
    axios.get('https://jsonplaceholder.typicode.com/users').then(response =>{
        // console.log(response.data)
        return response.data
        })
        .then (data =>{
            var mcbh = L.marker([21.460298, -157.763491]).addTo(mymap); 
            mcbh.bindPopup('<a href="http://127.0.0.1:8000/imageloader">Kaneohe Marine Corps Base </a>').openPopup();
            mcbh.on('mouseover', function (ev){mcbh.openPopup()})
            var hickam = L.marker([21.317407, -157.951014]).addTo(mymap); 
            hickam.bindPopup('Hickam AFB Beach').openPopup();
            hickam.on('mouseover', function ()
            {console.log('aaaaaaa')})

    }).catch(error=>{console.log('error', error)})
}

// function dakine(){
//     let kaneohe = 'kaneohe'
//     // if (icon.hasChildNodes){
//     //     icon.innerText = '';
//     // }
//     fetch(`https://api.openweathermap.org/data/2.5/weather?q=${kaneohe}&appid=8af2aa7fa978da0c3dc608a85406875c`)
// //   method: 'GET',
// //   headers: myHeaders,
// // })
//     .then(function(response){
//         return response.json()
//     })
//     .then(function(data){
//         console.log(data) 
//         console.log(data.wind.speed)
//         console.log(data.wind.deg)
//         let speed = document.getElementById('kaneohe_wind_speed')
//         speed.innerText = data.wind.speed;
//         //if you want to change to cardinal dir thats cool
//         let direction = document.getElementById('kaneohe_wind_direction')
//         direction.innerText = data.wind.deg;
//     })
//     .catch(function(error){
//         console.error('There has been a problem with your fetch operation:', error);
//     });
//     }

// function aiea(){
//         let aiea = 'aiea'
//         // if (icon.hasChildNodes){
//         //     icon.innerText = '';
//         // }
//         fetch(`https://api.openweathermap.org/data/2.5/weather?q=${aiea}&appid=8af2aa7fa978da0c3dc608a85406875c`)
//     //   method: 'GET',
//     //   headers: myHeaders,
//     // })
//         .then(function(response){
//             return response.json()
//         })
//         .then(function(data){
//             console.log(data) 
//             console.log(data.wind.speed)
//             console.log(data.wind.deg)
//             let speed = document.getElementById('hickam_wind_speed')
//             speed.innerText = data.wind.speed;
//             //if you want to change to cardinal dir thats cool
//             let direction = document.getElementById('hickam_wind_direction')
//             direction.innerText = data.wind.deg;
//         })
//         .catch(function(error){
//             console.error('There has been a problem with your fetch operation:', error);
//         });
//         }
// dakine()
// aiea()
















//without axios but still works 
// function myFunction(){
//     fetch('https://jsonplaceholder.typicode.com/users')
//     .then(function(response){
//         return response.json()
//     })
//     .then(function(data){
//         console.log(data);
//         let ul = document.getElementById('outputter');
//         for (let i = 0; i< data.length; i++) {
//             let name = data[i].name;
//             console.log(name)
//             let lat = data[i].address.geo; //gotta figu how to seperate lat and long
//             lat =Object.values(lat)
//             console.log(lat[0])
//             let long = data[i].address.geo;
//             long = Object.values(long);
//             console.log(long[1])
//             var marker = L.marker([`${lat[0]}`,`${long[1]}`]).addTo(mymap); 
//             marker.bindPopup( `<b>Name: ${name}</br><b>Long: ${long}</b><br>Lat: ${lat}`).openPopup();
//             let li = document.createElement('li');
//             li.innerText+=`Name: ${name}, Long: ${long}, Lat: ${lat}`
//             ul.appendChild(li)
//         }
//     })
// }