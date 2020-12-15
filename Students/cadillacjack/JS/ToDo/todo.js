let addIt = document.getElementById('btn-1');
let moveIt = document.getElementById('btn-2');
let removeIt = document.getElementById('btn-3');

let incomplete = document.getElementById('toDoList')
let complete = document.getElementById('complete')
let text = document.getElementById('text-field')

addIt.addEventListener('click',function(){
    const li = document.createElement('li')
    li.style.listStyle = "none";
    const check = document.createElement('input');
    check.setAttribute('type', 'checkbox');
    let doit = incomplete.appendChild(li);
    let checkit = li.append(check)
    doit.innerHTML += ' ' + text.value;
    
    
    removeIt.addEventListener('click',function(){
        for(let i=0; i<incomplete.children.length; i++){
            if (li.children[0].checked){
                li.children[0].checked=false;
                console.log('Make Money Money')
                incomplete.removeChild(li) 
                console.log(incomplete)
            }
        }
    })
    moveIt.addEventListener('click',function(){
        for(let i=0; i<incomplete.children.length; i++){
            if (li.children[0].checked){
                li.children[0].checked=false;
                const lis = document.createElement('li')
                lis.style.listStyle = "none";
                let doitb = complete.appendChild(lis);
                console.log("work?")
                doitb.innerHTML += `
                <img class=checkPic width=35px src='media/checkbox.jpg'>
                ${li.innerText}`;
                incomplete.removeChild(li)
            }
        }
    })
})






