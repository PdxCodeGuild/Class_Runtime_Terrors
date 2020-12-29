let addinput = document.getElementById('inputter')
let addbtn= document.getElementById('buttoner')
let adddiv = document.getElementById('div1')

addbtn.addEventListener('click', function(){
  var paragraph = document.createElement('p');
  paragraph.innerText = addinput.value;
  adddiv.appendChild(paragraph);
  inputter.value=''
  paragraph.addEventListener('click', function(){
    paragraph.style.textDecoration = 'line-through'
  paragraph.addEventListener('dblclick', function(){
    adddiv.removeChild(paragraph)
  })
  })
})
