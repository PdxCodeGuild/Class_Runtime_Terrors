## Promises

A Promise is an object representing the eventual completion or failure of an asynchronous operation. What does asynchronous mean?

Javascript is a single threaded language. This means that it executes code in order and must finish executing a piece code before moving onto the next. For instance, take a look at this code:

```javascript
console.log(1)
console.log(2)
console.log(3)
```
As expected, the code above will be executed in the order in which is written or *synchronously*. This represents a limitation, especially working with HTTP requests. Let's imagine that you are visiting a page and in the background there's an HTTP request to the server that is taking too long. Imagine that the browser can load all the elements in the page, including buttons, text, images only after that the HTTP request has finished running. This would cause the visitor to leave and would be a terrible user experience. Promises are one of the methods that Javascript uses to solve this problem,they make code run *asynchronously*


