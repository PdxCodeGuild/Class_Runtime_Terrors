/**
 * 
 * Use the favqs.com api to show a random quote. To start, use https://favqs.com/api/qotd to GET a quote, then display it on the page.

{
  "id": 4,
  "author": "Albert Einstein",
  "body": "Make everything as simple as possible, but not simpler.",
  ...
}
Version 2
The API also supports browsing quotes. You can use the page and filter parameters to get a bunch of quotes. You can add page buttons and/or a text input field and button for filtering.

"https://favqs.com/api/quotes?page="+page_id+"&filter=" + text. For example, you could use this syntax:

https://favqs.com/api/quotes?1&filter=mark


 */
const URL = "https://favqs.com/api/qotd";
const URL2 = "https://favqs.com/api/quotes?1&filter=";

function http_get(url, success) {
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState === 1) {
      xhttp.setRequestHeader("Authorization", `Token token=${API_KEY}`);
    } else if (this.readyState === 4 && this.status === 200) {
      let data = JSON.parse(xhttp.responseText);
      success(data);
    } else if (this.readyState === 4 && this.status === 404) {
      return "err";
    }
  };
  xhttp.open("GET", url);
  xhttp.send();
}

const quote = document.getElementById("quote");

http_get(URL, data => {
  console.log(data);
  quote.innerHTML = data?.quote?.body || "err";
});

// V2
const q = document.getElementById("input");
const qBtn = document.getElementById("inputBtn");
qBtn.onclick = () => {
  const query = q.value;
  if (!query) return;
  const url = URL2 + encodeURIComponent(query);
  http_get(url, data => {
    console.log(data);
    const { quotes } = data;
    if (!quotes || !Array.isArray(quotes)) return;
    quotes.map(q => {
      const li = document.createElement("li");
      li.innerHTML = q.body;
      quote.appendChild(li);
    });
  });
};
