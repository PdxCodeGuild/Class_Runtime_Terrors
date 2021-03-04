function getInfo() {
    let randomNum = Math.floor(Math.random() * 88 + 1)
    let apiUrl = 'https://www.swapi.tech/api/people/' + randomNum
    axios.get(apiUrl).then(function(response){
        updateInfo(response.data)        
    })
}
function updateInfo(data) {
    console.log(data)
    let name                 = document.getElementById('name')
        name.innerText       = `Name: ${data.result.properties.name}`
    let height               = document.getElementById('height')
        height.innerText     = `Height in Centimeter: ${data.result.properties.height}`
    let birth_year           = document.getElementById('birth_year')
        birth_year.innerText = `Birth year - Before the Battle of Yavin (BBY) : ${data.result.properties.birth_year}`
    let mass                 = document.getElementById('mass')
        mass.innerText       = `Mass in Kilogram: ${data.result.properties.mass}`
}
button.addEventListener('click', getInfo)