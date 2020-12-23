// var card = document.querySelector('.card');
// card.addEventListener( 'click', function() {
//   card.classList.toggle('is-flipped');
// });

// var card = document.getElementsByClassName('card');

// document.getElementById('s_one').addEventListener('click', function() {
//     card.classList.toggle('is-flipped');
// });

var card = document.querySelector('.card');
var button = document.getElementById('s_one')

button.addEventListener( 'click', function() {
  card.classList.toggle('is-flipped');
});