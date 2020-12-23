let apiKey = myKey;
let locData = null
function displayLoc(data){
    console.log(data);
    locData = data;

}
function displayUserStats (){
let city = locData.city;
let state = locData.state_prov;
let ip = locData.ip;
let flag = locData.country_flag;
let isp = locData.isp;
let lon = locData.longitude;
let lat = locData.latitude;




}

let init = { method:'GET',
            credentials: 'same-origin'};
function getLoc(){
    fetch(`https://api.ipgeolocation.io/ipgeo?apiKey=${myKey.KEY}`, init)
        .then(response => response.json())
        .then(showData => displayLoc(showData));

}

getLoc();
displayLoc();
//displayUserStats();