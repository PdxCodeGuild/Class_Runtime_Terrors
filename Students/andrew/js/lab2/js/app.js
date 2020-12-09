
function addItem(){
    let newElement = document.createElement('li');
  newElement.textContent = "I am a new element";
  let list = document.getElementById("my-list");
  }
  
  function addTodo(){
     let ul = document.getElementById("ul-content")
     let li = document.createElement("li");
     let btn = document.createElement('button');
     let todo = document.getElementById("inputfield").value;
     let text = document.createTextNode(todo);
     btn.innerText = "clear";
     li.appendChild(text);
     li.appendChild(btn);
     btn.setAttribute('onclick', 'clearItem()');
     if(todo === ''){
        alert('Please add text.')
     }
     else{
        document.getElementById("ul-content").appendChild(li).setAttribute('class', 'clear-btn');
        document.getElementById("li").appendChild(btn);
    }
    
  }


  function clearItem(){
     
  }
  
  function clearList(){
    let ul = document.getElementById("ul-content");
    let li = document.createElement('li');
    let i;
    console.log(ul.children.length);
  
    for ( i = ul.children.length; i > 0; i--){
      ul.innerHTML = "";
    }
    
  }
  
  
  function complete(){
        let list = document.querySelector('ul');
        list.addEventListener('click', function(ev) {
         if (ev.target.tagName === 'LI') {
           ev.target.classList.toggle('checked');
           let sp = document.createElement('span');
           sp.innerText = "Completed";
           ev.target.appendChild(sp);
           isComplete = true;  
         }
       }, false);
      
  }

 
  

 
  

  
  
  