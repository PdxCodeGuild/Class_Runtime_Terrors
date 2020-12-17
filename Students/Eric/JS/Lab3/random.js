const eList = ['https://www.bing.com/', 'https://search.creativecommons.org/', 'https://duckduckgo.com/', 'https://www.searchencrypt.com/home', 'https://www.google.com', 'https://www.msn.com/', 'https://www.yahoo.com/']


const myForm = document.getElementById("clickme");
myForm.addEventListener("click", (e) =>{
    let pick = Math.floor(Math.random() * 7);
    window.location.href = eList[pick]
})
