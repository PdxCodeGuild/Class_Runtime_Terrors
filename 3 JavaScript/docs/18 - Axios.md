## Axios

Axios is a popular, promise-based HTTP client that sports an easy-to-use API and can be used in both the browser and Node. js. Making HTTP requests to fetch or save data is one of the most common tasks a client-side JavaScript application will need to do. Axios is recommended over *fetch* for its wider browser support.

[Axios official documentation](https://github.com/axios/axios/blob/master/README.md)

```javascript
async function sendGetRequest() {
  try {
    const resp = await axios.get(
      "https://jsonplaceholder.typicode.com/todos/1"
    );
    console.log(resp.data);
  } catch (err) {
    // Handle Error Here
    console.error(err);
  }
}
sendGetRequest();
```

It can also be written with the arrow syntax:

```javascript
const axios = require("axios");

const sendGetRequest = async () => {
  try {
    const resp = await axios.get(
      "https://jsonplaceholder.typicode.com/todos/1"
    );
    console.log(resp.data);
  } catch (err) {
    // Handle Error Here
    console.error(err);
  }
};

sendGetRequest();
```

You can also use a more promise-based format:

```javascript
function sendGetRequest() {
  axios.get("https://jsonplaceholder.typicode.com/todos/1").then((res) => {
    console.log(res.data);
  });
}

sendGetRequest();
```
