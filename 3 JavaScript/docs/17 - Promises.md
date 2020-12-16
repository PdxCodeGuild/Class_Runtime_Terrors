## Promises


A Promise is an object representing the eventual completion or failure of an asynchronous operation. What does asynchronous mean?

Javascript is a single threaded language. This means that it executes code in the order in which it was written, and it must finish executing a piece of code before moving onto the next. For instance, take a look at this code:

```javascript
console.log(1)
console.log(2)
console.log(3)
```

As expected, the code above will be executed in the order in which is written or *synchronously*. This represents a limitation, especially working with HTTP requests. Let's imagine that you are visiting a page and in the background there's an HTTP request to the server that is taking too long to run. Imagine that the browser can load all the elements in the page, including buttons, text, images only after that the HTTP request has finished running. This would cause the visitor to leave and would be a terrible user experience. 

Promises are one of the methods that Javascript uses to solve this problem, they make code run *asynchronously*. That's how you write a promise:

```javascript
let promise = new Promise(function(resolve, reject) {
  // do a thing, possibly async, then…

  if (2+3 == 4) {
    resolve("Stuff worked!");
  }
  else {
    reject(Error("It broke"));
  }
});

```

The promise constructor takes one argument, a callback with two parameters, resolve and reject. Do something within the callback, perhaps async, then call resolve if everything worked, otherwise call reject. In this case the promise will be rejected because 4 isn't equal to 2+3.

Here's how you use that promise:

```javascript
promise
    .then(function(result){
        console.log(result); // "Stuff worked!"
    })
    .catch(function(err){
        console.log(err); // Error: "It broke"
    })
```
*then()* takes two arguments, a callback for a success case, and another for the failure case. Both are optional, so you can add a callback for the success or failure case only.

The code below is a good example of how promises allow asynchronous code to run:

```javascript
console.log('Hello Promise');
let p = new Promise((resolve, reject)=> {
 console.log('Promise started working');
 console.log('Promise is doing some important work…');
 console.log('Promise has completed, about to resolve');
 resolve('Promise resolved');
});
p.then((message) => { console.log('Resolved!!!')} );
console.log('Normal work flow');
let count = 0
for (let i = 0; i < 10000; i++) {
 count += 1;
}
console.log('Count: ', count);
setTimeout(() => {console.log('Timed out');}, 0);
console.log('Goodbye dear Promise');
```

Let's take a closer look to a real API call with Promises using an XMLHttpRequest:

```javascript
let promise = new Promise(function(resolve, reject) {
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", 'https://jsonplaceholder.typicode.com/todos/1');
    xhttp.onload = function() {
        if (this.readyState === 4 && this.status === 200) {
            resolve(this.responseText);
        } else {
            reject('error')
        }
    };
    xhttp.onerror = function() {
        reject({
            status: this.status,
            statusText: xhttp.statusText
        });
    };
    xhttp.send();
});

promise
    .then((result) => {
        console.log("Resolve method: ", result);
    })
    .catch((error) => {
        console.error("Catch Method: ", error);
    });

```

Here's a more modern way to handle API calls using promises with fetch:

```javascript
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
  });

```

Axios is preferred over fetch for its wider support. Axios is a popular, promise-based HTTP client that sports an easy-to-use API and can be used in both the browser and Node. For more information, consult the document n.18 *Axios*


