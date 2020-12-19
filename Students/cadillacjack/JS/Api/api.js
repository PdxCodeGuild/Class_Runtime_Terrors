let $reLoad = $('#reloadBtn')

function myFunc(data){
    let $body = $('body');
    let $h1 = "<h1 id='author'>"+"Here is a quote from " + data['quote']['author'] + "</h1>";
    let $h2 = "<h2 id='quote'>"+ data['quote']['body'] + "</h2>";
    console.log($h1);
    $body.append($h2).css({'text-align': 'center'});
    $body.append($h1);
}

fetch('https://favqs.com/api/qotd')
  .then(response => response.json()) //1st "then" will always return the "response". Can be called anything
  .then(data => myFunc(data)) // 2nd "then" will always return the data from 1st "then". Can be called anything
  .catch(error => {
      console.error('There has been a problem with your fetch operation:', error);
    });

$reLoad.on('click', function(){
  console.log("action")
  location.reload(this)
})


