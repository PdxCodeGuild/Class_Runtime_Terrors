function getRandomInt(max) {
    return Math.floor(Math.random() * 99) + 1;  // returns a random integer from 1 to 99
  }
  


  var text = "";
  var wpick6 = [];
  var i;
  
  for (i = 0; i < 6; i++) {
    wpick6.push(getRandomInt(99));
  }

  console.log(wpick6);
