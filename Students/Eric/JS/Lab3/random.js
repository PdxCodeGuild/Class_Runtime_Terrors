const eList = ['https://www.bing.com/', 'https://search.creativecommons.org/', 'https://duckduckgo.com/', 'https://www.searchencrypt.com/home', 'https://www.google.com', 'https://www.msn.com/', 'https://www.yahoo.com/']

function myFunction() {
    let pick = Math.floor(Math.random() * 7);
    window.location.href = eList[pick]
  }

const myForm = document.getElementById("clickme");
const myForm2 = document.getElementById("5sec");

myForm.addEventListener("click", (e) =>{
    myFunction();
})

myForm2.addEventListener("click", (e) =>{
    setTimeout(myFunction, 5000)
})
