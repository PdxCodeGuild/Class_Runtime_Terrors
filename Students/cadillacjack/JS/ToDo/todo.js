let a = document.getElementById('btn-1');
let b = document.getElementById('btn-2');
let c = document.getElementById('btn-3');

let incomplete = document.getElementById('toDoList')
let complete = document.getElementById('complete')
let text = document.getElementById('text-field')

a.addEventListener('click',function(){
    const li = document.createElement('li')
    li.style.listStyle = "none";
    const check = document.createElement('input');
    check.setAttribute('type', 'checkbox', 'value', text.value);
    let doit = incomplete.appendChild(li);
    let checkit = li.appendChild(check)
    doit.innerHTML += text.value;
    
    
})

b.addEventListener('click',function(){
    const li = document.createElement('li')
    li.style.listStyle = "none";
    let doitb = complete.appendChild(li);
    console.log("work?")
    doitb.innerHTML += `
    <img class=checkPic width=35px src='media/checkbox.jpg'>
    ${text.value}`;
    
    
})
c.addEventListener('click',function(){
    let ol = document.getElementById('toDoList')
    let li = ol.children
    console.log(ol)
    for(let i=0; i<li.length; i++){
        if (li[i].children[0].checked){
            let trash = li[i]
            trash.innerHTML = ''
            console.log(trash)
        }
    }


    // let checkit = li.splice(check)
    // let doit = incomplete.splice(li);
    // doit.innerHTML += text.value;
})
