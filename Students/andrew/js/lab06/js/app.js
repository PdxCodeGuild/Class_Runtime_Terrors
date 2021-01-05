
let mymap = L.map('mapid').setView([42, -100], 3);
let key = myKey;
let count = 0;
let Users = {};

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=' + key.KEY, {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 8,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'your.mapbox.access.token'
}).addTo(mymap);

let marker = L.marker([42, -100]).addTo(mymap);

const nextBtn = document.getElementById('next-btn');
nextBtn.addEventListener('click', e =>{
    nextLoc();
})

const nextLoc = async () => {

    let Users = await getUsers();

    if (count < Users.length) {
        let index = count;
        displayUser(Users, index)
        count++;
        if (count === 10) {
            alert("You have reached the end of the list.");
            count = 0;
            mymap.eachLayer((layer) => {
                if (layer._url === undefined) {
                    layer.remove();
                }
            });

        }
    }

}



const getUsers = async () => {
    try {
        const response = await axios.get('https://jsonplaceholder.typicode.com/users');
        let usr = response.data;

        return usr;
    } catch (e) {
        console.log(e);
    }


};


const displayUser = (allUsers, index) => {
    
    populateSidebar(allUsers , index)
    console.log(allUsers[index]);
    let loc = allUsers[index].address.geo;
    console.log(loc);
    let marker = L.marker(loc).addTo(mymap);
    mymap.flyTo(loc);
    let popup = L.popup()
        .setLatLng(loc)
        .setContent(`<p>Name: ${allUsers[index].name}</p>`)
        .openOn(mymap);
    marker.bindPopup(`<p>Name: ${allUsers[index].name} Lat: 
        ${allUsers[index].address.geo.lat} 
        Lon: ${allUsers[index].address.geo.lng} Company Slogan:
        ${allUsers[index].company.catchPhrase}</p>
        `).openPopup();
}

const populateSidebar = (user, i) => {
    let curName = "";
    let curEmail = "";
    let curCity = "";
    let curPhone = "";
    let curWeb = "";

    curName = user[i].name;
    curEmail = user[i].email;
    curCity = user[i].address.city;
    curPhone = user[i].phone;
    curWeb = user[i].website;
    

    const name = document.querySelector('#name');
    const email = document.querySelector('#email');
    const city = document.querySelector('#city');
    const phone = document.querySelector('#phone');
    const website = document.querySelector('#website');

    name.innerText = "Name: ";
    email.innerText = "Email: ";
    city.innerText = "City: ";
    phone.innerText = "Phone: ";
   website.innerText = "Website: "

    name.append(curName);
    email.append(curEmail);
    city.append(curCity);
    phone.append(curPhone);
    website.append(curWeb);


    
    
}


