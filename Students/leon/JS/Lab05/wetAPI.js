let key = getKey()

btn.addEventListener('click', function() {
      
       let bev = document.createElement('img')
       bev.id = 'bev'

        let input = document.getElementById('name')
        let name = input.value.toLowerCase()
        let btn = document.getElementById('btn')
        let info = document.getElementById('info')

        fetch("https://api.openweathermap.org/data/2.5/weather?q=" + name + "&units=imperial&appid=" + key)
        .then(response => response.json())
        .then(data => {
                console.log(data)
                console.log(data["main"])
                console.log(data["main"]["temp"])

                if(data["main"]["temp"] <= 72) {
                        console.log("Cold")
                        bev.src = "hotcoffee.png"
                       document.body.appendChild(bev)
                } else {
                        console.log("Hot")
                        bev.src = "icedcoffee.png"
                        document.body.appendChild(bev)
                }
                
                console.log('Current Temp in ' + name + ': ' + Math.round(data["main"]["temp"]))
                info.innerText = 'Current Temp in ' + name.toUpperCase() + ': ' + Math.round(data["main"]["temp"])
        })
        .catch(error => {console.error('there was an error ', error)});

})
    
   


 


       
