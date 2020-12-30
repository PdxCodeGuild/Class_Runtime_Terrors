let apiKey = myKey;
let apiKey2 = myKey2;

function displayUserStats(data) {
    if(data === undefined){
        console.log('waiting for data')
    }else{

    
    let locData = data;
   
    
    let city = locData.city;
    let displayCity = document.getElementById('city');

    let state = locData.state_prov;
    let displayState = document.getElementById('state');

    let ip = locData.ip;
    let displayIp = document.getElementById('ip');
    let flag = locData.country_flag;
    let isp = locData.isp;
    let displayIsp = document.getElementById('isp')
    let lon = locData.longitude;
    let lat = locData.latitude;
    let displayLon = document.getElementById('lonlat');

    
    displayCity.innerHTML = city;
    displayState.innerHTML = state;
    displayIp.innerHTML = ip;
    displayIsp.innerHTML = isp;
    displayLon.innerHTML = "longitude " + lon +" "+"Latitude "+  lat;
    

    }

}

function displayUser(foo){
    let pic = foo.data[0].picture
    let element = document.createElement('img');
    element.setAttribute('src', pic);
    element.setAttribute('alt', 'profile picture');
    element.setAttribute('height', '150');
    element.setAttribute('width','150')
    let profilePic = document.getElementById('profile-pic').appendChild(element);
    
    console.log(pic);

}

let init = {
    method: 'GET',
    credentials: 'same-origin',
    
};

 function getLoc() {
    fetch(`https://api.ipgeolocation.io/ipgeo?apiKey=${apiKey.KEY}`, init)
        .then(response => response.json())
        .then(showLocation => displayUserStats(showLocation))
        .catch(error => console.error(error))

}


function getUser() {
    
    fetch('https://dummyapi.io/data/api/user', {headers: {'app-id': `${apiKey2.KEY2}`}})
    .then(response => response.json())
    .then(showUser => displayUser(showUser))
    .catch(error => console.error(error))

    
}




getLoc();
displayUserStats();
getUser();