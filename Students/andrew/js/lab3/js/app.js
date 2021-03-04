let count = 5;

function countdown(){
    let countdown = setInterval(fivesec, 1000);
}


function redirect(){
    
    let urls = ['https://www.google.com', 'https://www.yahoo.com','https://www.bing.com',
                'https://www.github.com', 'https://500px.com', 'https://www.apple.com'];
    let sitesCount = urls.length;

    let loc = Math.floor(Math.random() * Math.floor(sitesCount));
    
    location.assign(urls[loc]);
}

function fivesec(){
    document.getElementById("count-down").innerHTML = count;
    count--;
    if( count === 0){
        redirect();
    }
 }
 