let prettify = document.querySelector('#prettify')
let pText = prettify.textContent

const genRan = () => Math.floor(Math.random() * 255)

newHtml = ''
for(let char of pText) {
    let span = document.createElement('span')
    span.innerText = char
    span.style.color = `rgb(${genRan()}, ${genRan()}, ${genRan()})`
    newHtml += span.outerHTML
}
prettify.innerHTML = newHtml

let cookieJar = document.querySelector('#cookie-jar')
let cookies = cookieJar.textContent
cookieJar.textContent = ''
document.querySelector('#cookie-plate').textContent = cookies

url = 'https://randomuser.me/api/'

axios.get(url)
    .then(request => {
        data = request.data.results[0]
        let {name, login, email, phone, location} = data
        let newDeets = document.querySelector('#new-deets')
        newDeets.innerHTML = `
            <li>name: ${name.first}</li>
            <li>username: ${login.username}</li>
            <li>email: ${email}</li>
            <li>phone: ${phone}</li>
            <li>street: ${location.street.number}  ${location.street.name}</li>
            <li>city: ${location.city}</li>
            <li>state: ${location.state}</li>
            <li>zip: ${location.postcode}</li>
        `
    })
    .catch(error => console.log(error))