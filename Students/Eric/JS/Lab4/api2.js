

// var dataSaver = null;

function http_get(url, success) {
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
      if (this.readyState === 1) {
          xhttp.setRequestHeader('Authorization', 'Token token="83ff6c5e1850ac35856e1869206dd66e"')
      } else if (this.readyState === 4 && this.status === 200) {
          let data = JSON.parse(xhttp.responseText);
          // dataSaver = data
          success(data);
          return data
      } else if (this.readyState === 4 && this.status === 404) {
          // handle 404
      }
  };
  xhttp.open("GET", url);
  xhttp.send();
}

http_get("https://favqs.com/api/quotes",display)

let dataSaver = http_get("https://favqs.com/api/quotes",display);

function display(data){
  
  console.log(data)
  dataSaver = data.quotes
  
}

const element1 = document.querySelector("#output1")
const element2 = document.querySelector("#output2")
const myForm = document.getElementById("pick-form");
myForm.addEventListener("submit", (e) =>{
  e.preventDefault(); // Prevents from auto sumbiting
  const getNum = document.getElementById('uNum').value
  console.log(getNum);

  try{
  element1.innerHTML = (`The Aurthor is ${dataSaver[getNum]["author"]}`)
  element2.innerHTML = (`The Quote is ${dataSaver[getNum]["body"]}`)
  }
  catch(err){
  alert('Out Range')
  }
})

const myForm2 = document.getElementById("clearbut");
myForm2.addEventListener("click", (e) =>{
  e.preventDefault();
  element1.innerHTML = ('')
  element2.innerHTML = ('')
})


// const form = document.getElementById('name-form')
// form.addEventListener('submit', e => {
//   e.preventDefault()
//   console.log(form.number-pick)
//   // if (listName == null || listName === '') return
// })

// form.onsubmit = function(e){
//   e.preventDefault();
//   console.log(form.number-pick);
// }

// function buttonClick(){
//   event.perventDefault(event)
//   console.log("Check")
//   const inputElement = document.querySelector("#valve")
//   const value = inputElement.value
//   console.log(value,inputElement)



// }

