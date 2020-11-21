url = 'https://favqs.com/api/quotes'
axios.get(url, {
        headers: {
            'Authorization': `Token token="${myKey}"`
        }
  })
  .then(response => {
      data = response.data.quotes
      data.forEach(element => {
      newDiv1 = document.createElement('div')
      newDiv1.classList.add('item')
      newDiv1.innerText = element.body

      newDiv2 = document.createElement('div')
      newDiv2.classList.add('item')
      newDiv2.innerText = element.author

      quoteContainer = document.getElementById('quote-container')
      quoteContainer.appendChild(newDiv1)
      quoteContainer.appendChild(newDiv2)
      }
  )})
  .catch(error => {
    console.log(error)
  })