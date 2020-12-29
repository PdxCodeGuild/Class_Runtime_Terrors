let addinput = document.getElementById('inputter')
let addbtn= document.getElementById('buttoner')
let adddiv = document.getElementById('outputField')

addbtn.addEventListener('click', function(){
  var paragraph = document.createElement('p');
  paragraph.classList.add('paragraph-styling');
  paragraph.innerText = addinput.value;
  adddiv.appendChild(paragraph);
  inputter.value=''
  paragraph.addEventListener('click', function(){
    paragraph.style.textDecoration = 'line-through';
  paragraph.addEventListener('dblclick', function(){
    adddiv.removeChild(paragraph)
  })
  })
})



// let dis = []

// function dakine(){
//   let lister = dis.map(user =>`<li>${user}</li>`).join('\n')
                               
                            
//   document.querySelector('ul').innerHTML = lister
// }

// let addbtn = document.querySelector('button')
// let inputter = document.querySelector('input')

// addbtn.addEventListener('click', ()=>{
//   dis.push(inputter.value);
//   // let ugh = document.getElementById('bjork');
//   // ugh.innerHTML = dis;
//   inputter.value = '';
//   dakine()
// })
