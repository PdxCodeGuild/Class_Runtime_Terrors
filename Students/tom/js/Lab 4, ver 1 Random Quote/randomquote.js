function randonQuote(author, quote) {
    document.getElementById('author').innerHTML = author
    document.getElementById('quote').innerHTML = quote
  }
  
  function getQuote(randonQuote) {
    let req = new XMLHttpRequest();
    req.open('GET', "https://favqs.com/api/qotd");
    req.onload = function() {
      if (req.status == 200) {
        let newQuote = JSON.parse(this.responseText)
        quoteAuthor = newQuote.quote.author
        quoteQuote = newQuote.quote.body
        randonQuote(quoteAuthor, quoteQuote);
      } else {
        randonQuote("Error: " + req.status);
      }
    }
    req.send();
  }
  
  getQuote(randonQuote);