const myHeaders = new Headers();
let key = getKey()
myHeaders.append('Authorization', `Token token="${key}"`);

function getAuth(some) {
    let auth = document.getElementById('author').innerText=some 
}

function getQuote(some) {
    let auth = document.getElementById('body').innerText=some 
}

function getId(some) {
    let auth = document.getElementById('iddy').innerText=some 
}


// make button go Go!
let btn = document.getElementById('btn')

btn.addEventListener('click', function() {
    // capture user input at input field 'search'
    // this will be used to search by page
    let input = document.getElementById("input")
    // let output = document.getElementById("body")
    // output.innerText = input.value
    let text = input.value
    let page_id = "1"
    //console.log(page)
    //console.log(key)
        fetch("https://favqs.com/api/quotes?page="+page_id+"&filter=" + text, {
            method: 'GET',
            headers: myHeaders,
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            console.log(typeof(data))
            console.log(data["quotes"]["0"]["author"])
            getAuth(data["quotes"]["0"]["author"])
            getQuote(data["quotes"]["0"]["body"])
            getId(data["quotes"]["0"]["id"])
        })
        .catch(error => {
            console.error('there was an error ', error)
        });

})
    
   


 

