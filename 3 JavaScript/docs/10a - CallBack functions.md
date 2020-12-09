## Call Back Functions

A callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.

```javascript
function greeting(name) {
  alert('Hello ' + name);
}

function processUserInput(greeting) {
  var name = prompt('Please enter your name.');
  greeting(name);
}

//passing the function greeting into processUserInput
processUserInput(greeting);

```

Because callback functions are functions passed into other functions, you can see them in the doc n.16 with map, sort, reduce and filter. 

Here's onother clear example of a callback function:

```javascript
let arr = [1, 2, 3, 4, 5];

function printItem(item, index) {
    console.log(`index: ${index} value: ${item}`);
}
arr.forEach(printItem);
```

The *forEach()* method executes a provided function once for each array element. So, for each element, we are running the function *printItem*

Compare the above function with the one below:

```Javascript
let arr = [1,2,3,4];

function printItem(item) {
  for (let i =0; i < item.length; i++){
   console.log(`index: ${i} value: ${item[i]}`}
}
printItem(arr)
```

Let's make another example:

```html
<button id="btn">Save</button>
<script>
   function btnClicked() { 
   // do something here
}
    let btn = document.querySelector('#btn');
    btn.addEventListener('click', btnClicked);
</script>
```

Which would be the equivalent of:

```javascript
let btn = document.querySelector('#btn');
btn.addEventListener('click', function() { 
   // do something here
   //using an anonimous function as well
});
```
