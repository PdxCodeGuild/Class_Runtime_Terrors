function addItem(){
    var ul = document.getElementById("to_do")
    var ul2 = document.getElementById('completed')
    var input = document.getElementById("input")
    var li = document.createElement("li")

    var del_button = document.createElement('button')
    del_button.innerText = 'Delete'
    del_button.onclick = function() {
        this.parentElement.remove()
    }

    var clickable = document.createElement('a')
    clickable.innerText = input.value
    clickable.setAttribute('id', input.value)
    
    li.setAttribute('id', input.value)
    li.appendChild(clickable)
    li.appendChild(del_button)
    ul.appendChild(li)

    clickable.onclick = function() {
        if (this.parentElement.parentElement === document.getElementById('to_do')){
            ul2.appendChild(this.parentElement)
        }
    }
}