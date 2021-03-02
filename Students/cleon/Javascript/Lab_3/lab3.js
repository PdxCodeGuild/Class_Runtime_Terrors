let urlList = ['https://threatpost.com/', 'https://pdxcodeguild.com/', 'https://www.wired.com/tag/cybersecurity/',
'https://www.youtube.com/'],

function randWeb() {
    let ranNum = Math.floor(Math.random() * 4);
    window.location.href = urlList[ranNum]

    }

let x = document.getElementById("butt");

x.addEventListener("click",  () => {
    setTimeout(randWeb(), 5000)

})