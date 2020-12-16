
function addItem(){
  let newElement = document.createElement('li');
  newElement.textContent = "I am a new element";
  let list = document.getElementById("my-list");
  }
  
  function addTodo(){
     let li = document.createElement("li");
     let dv = document.createElement("div");
     let clearBtn = document.createElement('button');
     let completeBtn = document.createElement('button');
     let todo = document.getElementById("inputfield").value;
     let text = document.createTextNode(todo);

     clearBtn.innerText = "clear";
     completeBtn.innerText = "complete";
     dv.innerText = todo;
     li.appendChild(dv);
     li.appendChild(clearBtn);
     li.appendChild(completeBtn);

     //completeBtn.setAttribute('onclick', 'parentElement.style.text-decoration = "line-through"');
     completeBtn.addEventListener('click', function(){
     dv.style.setProperty("text-decoration", "line-through");
      })


     clearBtn.setAttribute('onclick', 'parentElement.style.display = "none"');
     

     if(todo === ''){
        alert('Please add text.')
     }
     else{
        document.getElementById("ul-content").appendChild(li).setAttribute('class', 'btn');
        
        
    }
    
  }

function complete(){
  let btn = document.getElementsByClassName('btn');
  console.log(btn.parentElement);
}

  
  function clearList(){
    let ul = document.getElementById("ul-content");
    let i;
    for ( i = ul.children.length; i > 0; i--){
      ul.innerHTML = "";
    }
    
  }
  
  
  

  
  
  