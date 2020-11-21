# callbacks
a callback is nothing more than a function that is passed into another function as a parameter, and run inside the body of the function. read that last sentence a few more times to let that sink in before moving forward.

you've already seen several examples of callbacks, and may not have realized we were using them. for example, the following code from [this MDN article](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function) uses a callback:

```javascript
function greeting(name) {
  alert('Hello ' + name);
}

function processUserInput(callback) {
  var name = prompt('Please enter your name.');
  callback(name);
}

processUserInput(greeting);
```

in this example, `processUserInput` takes in a function as a parameter. in this case it is passed `greeting`. when `processUserInput` executes, a prompt shows up in the browser asking for the user's name. once the user submits their name, the function `callback` executes with the user's input as a parameter. since this function is passed into `processUserInput` and executed within `processUserInput`, it is a callback function (in case the subtle name didn't give it away). `callback` executes and pops up an alert displaying the user's name in the browser.

we can write our own code to use callbacks. JavaScript makes heavy use of clalbacks in its built-in methods, and many libraries and frameworks also make heavy use of callbacks. for example, the `forEach` array method uses a callback function to perform some task on each item of an array. the simple example below demonstrates this:
```javascript
arr = [1, 2, 3, 4, 5];

function printItem(item, index) {
    console.log(`index: ${index} value: ${item}`);
}

arr.forEach(item, printItem);
```
the `forEach` array method executes the callback function (in this case `printItem`) once for each item in the array. the [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#Syntax) has a good article on the method and its syntax. 

JavaScript and its libraries/frameworks are lousy with callbacks. they are **everywher**e. the primary use of callbacks in JavaScript is to handle asynchronous code. we won't cover this in detail, but we will touch on it when we get to making API requests.

Oftentimes code using callbacks is written more succinctly using arrow functions:
```javascript
arr = [1, 2, 3, 4, 5];

arr.forEach((item, index) => console.log(`index: ${index} value: ${item}`))
```
it's worth wrapping your head around callbacks since, as previously mentioned, they are heavily used in JavaScript.
