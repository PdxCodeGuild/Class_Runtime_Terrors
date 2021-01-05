let request = new XMLHttpRequest();
request.open("GET", "https://api.covid19api.com/summary"); 
request.send();
request.onload = () => {
  console.log(request);
  if (request.status === 200) {
    // by default the response comes in the string format, we need to parse the data into JSON
    const dataApi = JSON.parse(request.response)
    const element = document.querySelector("#text1")
    element.innerHTML += dataApi['Global']['NewConfirmed']
    const element2 = document.querySelector("#text2")
    element2.innerHTML += dataApi['Global']['NewDeaths']
    const element3 = document.querySelector("#text3")
    element3.innerHTML += dataApi['Global']['NewRecovered']
    const element4 = document.querySelector("#text4")
    element4.innerHTML += dataApi['Global']['TotalConfirmed']
    const element5 = document.querySelector("#text5")
    element5.innerHTML += dataApi['Global']['TotalDeaths']
    const element6 = document.querySelector("#text6")
    element6.innerHTML += dataApi['Global']['TotalRecovered']
  } else {
    console.log(`error ${request.status} ${request.statusText}`);
  }
}
