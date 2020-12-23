let url = 'https://api.nasa.gov/planetary/apod?api_key=4sGZ9oQpr4FqOaBewnmjODONv5FPIoOYB4dq6acz'
const divPic = document.getElementById('picDiv')
const owner = document.getElementById('copyright')
const explanation = document.getElementById('explanation')
const searchBtn = document.getElementById('searchBtn')

function getData(){
    fetch(url)
    .then(response => response.json())
    .then(data => {
        pic = data['hdurl']
        title = data['title']
        descript = data['explanation']
        release = data['date']
        copyright = data['copyright']
        console.log(data)
        console.log(release)
        
        owner.innerHTML = "<a id='title'><b>"+title+"</b></a><br><a id='owner'><b>Image Credit and Copyright: </b>"+copyright+"</a>"
        divPic.innerHTML += "<p><b>"+release+"</b></p>"
        divPic.innerHTML += "<img class='pic' src="+pic+"></img>"
        explanation.innerHTML = "<b>Explanation: </b>"+descript
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
        });
}
getData()
searchBtn.addEventListener('click',function(){
    url = 'https://api.nasa.gov/planetary/apod?api_key=4sGZ9oQpr4FqOaBewnmjODONv5FPIoOYB4dq6acz'
    year = document.getElementById('years').value
    month = document.getElementById('months').value
    day = document.getElementById('days').value
    divPic.innerHTML = ""
    url = (url+"&date="+year+"-"+month+"-"+day)
    getData()
    
})