let key = api();
let left = document.getElementById("left");
let right = document.getElementById("right");
let page_number = 1;
let and_one = "";
let param_2 = "";
let current_page = "";
let page_data = undefined;
let test = "";
let quote_ul = document.getElementById("quote_ul");

refresh();

document.getElementById("right").addEventListener("click", function page_up() {
  if (page_data.last_page === false) {
    page_number += 1;
    page_builder();
    quote_ul.innerHTML = "";
    page_data = refresh();
  } else if (page_data.last_page === true) {
    console.log("last page");
  }
});

document.getElementById("left").addEventListener("click", function page_up() {
  if (page_data.page !== 1) {
    page_number -= 1;
    page_builder();
    quote_ul.innerHTML = "";
    page_data = refresh();
  } else if (page_data.page === 1) {
    console.log("first page");
  }
});

function page_builder() {
  current_page = "page=" + page_number.toString();
}

function refresh() {
  const myHeaders = new Headers();

  myHeaders.append("Authorization", 'Token token="' + key + '"');
  fetch(`https://favqs.com/api/quotes/?${current_page}${and_one}${param_2}`, {
    method: "GET",
    headers: myHeaders,
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      //or pass a callback function to handle data
      page_data = data;

      for (const property in page_data.quotes) {
        console.log(page_data.quotes[property]);
        let li = document.createElement("li");
        let p1 = document.createElement("p");
        let p2 = document.createElement("p");
        let p3 = document.createElement("p");
        let author = page_data.quotes[property].author;
        let body = page_data.quotes[property].body;

        if (page_data.quotes[property].source !== undefined) {
          var source = page_data.quotes[property].source;
          p3.innerText = source;
        }

        li.setAttribute("id", page_data.quotes[property].id);
        p1.innerText = author;
        p2.innerText = body;
        li.appendChild(p1);
        li.appendChild(p2);
        li.appendChild(p3);
        quote_ul.appendChild(li);
      }

      console.log(data);
    })
    .catch(function (error) {
      console.error(
        "There has been a problem with your fetch operation:",
        error
      );
    });
}
