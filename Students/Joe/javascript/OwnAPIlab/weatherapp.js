const myHeaders = new Headers();
const filter= document.getElementById('inputter');
// const url = `https://api.openweathermap.org/data/2.5/weather?q=${filter}&appid=8af2aa7fa978da0c3dc608a85406875c`;
myHeaders.append('Authorization',  'Token token="  8af2aa7fa978da0c3dc608a85406875c"');
let outputter = document.getElementById('outputter')

function dakine(){
    if (icon.hasChildNodes){
        icon.innerText = '';
    }
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${filter.value}&appid=8af2aa7fa978da0c3dc608a85406875c`)
//   method: 'GET',
//   headers: myHeaders,
// })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        console.log(data) 
        let temperature = document.getElementById('temperature')
        temperature.innerText = data.main.temp;
        let city = document.getElementById('city')
        city.innerText = data.weather[0].description;  
        if(data.weather[0].description.includes('clouds')){
            let icon = document.getElementById('icon')
            let div= document.createElement('div');
            div.classList.add('fas' ,'fa-cloud');
            icon.appendChild(div);   
        }  
        if(data.weather[0].description.includes('rain')){
            let icon = document.getElementById('icon')
            let div= document.createElement('div');
            div.classList.add("fas", "fa-cloud-rain");
            icon.appendChild(div);   
        } 
    })
    .catch(function(error){
        console.error('There has been a problem with your fetch operation:', error);
    });
    }