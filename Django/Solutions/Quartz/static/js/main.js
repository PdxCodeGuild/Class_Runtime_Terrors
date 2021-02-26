
    
    $(".fb-share-button").on("click", function(event) {
    if(event.target.tagName == 'BUTTON') {
        let url = event.target.closest('DIV').children[0].href
        let url2 = event.target.closest('DIV').children[0].dataset.href
          window.open(
              
            'https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(`${url2}`),'popUpWindow','height=500,width=400,left=100,top=100,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no, status=yes'
           
        )
    }   
})

$(".pinterest-share-button").on("click", function(event) {
    if(event.target.tagName == 'BUTTON') {
        let url = event.target.closest('DIV').children[0].href
        let url2 = event.target.closest('DIV').children[0].dataset.href
        // console.log(url2)
          window.open(
            ' http://www.pinterest.com/pin/create/button/?url=' + encodeURIComponent(`${url2}`) + '&media=' + encodeURIComponent(`${url2}`), 'popUpWindow','height=500,width=400,left=100,top=100,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no, status=yes'
           
        )
    }   
})

$(function() {
    $('[data-toggle="popover"]').popover({
          html: true,
          content: function() {
              return $('#popover-content').html();
          }
    });
  });

 
window.addEventListener('DOMContentLoaded', (event) => {

    let options = {
  
      root: null,
      rootMargin : '250px 0px',
      threshold: 0.5,
    }

    let observer = new IntersectionObserver (beTouching, options);

    document.querySelectorAll('.par').forEach(img => {
      
      observer.observe(img)
    })

    function beTouching(entries){
      entries.forEach(obj => {
        if(obj.isIntersecting){
          obj.target.classList.add('active')
          observer.unobserve(obj.target)
        }
      })
    }


})

fetch("http://127.0.0.1:8000/create/albums/")
.then((response) => {
  return response.json();
})
.then((data) => {
  console.log(data);
});
  




