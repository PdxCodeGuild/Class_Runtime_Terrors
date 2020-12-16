let request = new XMLHttpRequest();
request.open("GET", "https://favqs.com/api/qotd"); 
request.send();
request.onload = () => {
  console.log(request);
  if (request.status === 200) {
    // by default the response comes in the string format, we need to parse the data into JSON
    const dataApi = JSON.parse(request.response)
    const element = document.querySelector("#text1")
    element.innerHTML += dataApi["quote"]["author"]
    const element2 = document.querySelector("#text2")
    element2.innerHTML += dataApi["quote"]["body"]
  } else {
    console.log(`error ${request.status} ${request.statusText}`);
  }
}