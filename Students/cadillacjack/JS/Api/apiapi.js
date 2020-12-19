const myHeaders = new Headers();
let $reLoad = $('#reloadBtn');
let $ul = "<ul id='quotes'></ul>"
$(".work").append($ul)

function myFunc(data){
    console.log(data)
    let $quotes = $('#quotes')
    $quotes.empty()

    
    for (i=0; i<data['quotes'].length;i++){
        console.log('hey')
        let author = data['quotes'][i]['author']

        let saying = data['quotes'][i]['body']

        let directLink = data['quotes'][i]['url']

        let $li = "<li class="+"li"+i+">"+"<a"+" "+"target='_blank'"+" "+"href="+directLink+">"+'"'+saying+'"'+" "+"-" +author +"<a/></li>";
        
        $quotes.append($li)
        console.log($quotes)
    }

}

myHeaders.append('Authorization',  'Token token=""');

$reLoad.on('click', function(){
    let text = $('#input').val();
    let $page_id = $('#pageId').val();
    fetch("https://favqs.com/api/quotes?page="+$page_id+"&filter="+text, {
        method: 'GET',
        headers: myHeaders,
    })
    .then(function(response){
        return response.json()
    })
    .then(data => myFunc(data))
    
    .catch(function(error){
        console.error('There has been a problem with your fetch operation:', error);
    });
})