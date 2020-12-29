const sightList = ['https://youarenotsosmart.com/',
'https://video.search.yahoo.com/search/video?fr=mcafee&p=jesus+christ+superstar+soundtrack#id=2&vid=c3619bb9b7f2b69b658085814c3899c2&action=click',
'https://www.ancient.eu/socrates/',
'https://www.goodreads.com/author/show/66079.Sonia_Johnson',
'https://www.amazon.com/Better-Angels-Our-Nature-Violence/dp/1846140943'
]

let change = document.getElementById('randomChange');

function redirect() {
    let rotate = Math.floor(Math.random() * (5-0));
    console.log(sightList)
    let current = document.getElementById('current_page');
    location.href = sightList[rotate];
    console.log(sightList[rotate]);
    setInterval(redirect, 15000);
}

let count= 15 

function countClock(){
    document.getElementById('time').innerHTML= count;
    if (count===0){
        redirect()
    }
    count = count-1
}

change.addEventListener('click', function() {
    alert('Start random redirect?');
    setInterval(countClock, 1000);
})
