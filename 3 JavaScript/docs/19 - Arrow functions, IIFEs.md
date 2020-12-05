## Arrow functions

An arrow function expression is a compact alternative to a traditional function expression, but is limited and can't be used in all situations. You can read more [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

Let's take a look at a traditional anonymous function expression:

```Javascript
function (a){
  return a + 100;
}
```

With an arrow function we can remove the keyword `function` the `return` statement because it's implied, the curly brackets and the argument parenthesis. We get the following:

```Javascript
a => a + 100;
```

However, if you have multiple arguments, or no arguments, you'll need to add the parenthesis around the argument:

```Javascript
function (a,b){
  return a + b + 100;
}
```
becomes:

```Javascript
(a, b) => a + b + 100;
```

If you have multiple arguments:

```Javascript
let a = 4;
let b = 2;
function (){ 
  return a + b + 100;
}
```

It will become:


```Javascript
let a = 4;
let b = 2;
() => a + b + 100;
}
```

If the body requires additional lines of processing, you'll need to re-introduce brackets with the `return`

```Javascript
// Traditional Function
function (a, b){
  let chuck = 42;
  return a + b + chuck;
}
 
// Arrow Function
(a, b) => {
  let chuck = 42;
  return a + b + chuck;
}
```
Let's take a look at a named function:

```Javascript
// Traditional Function
function bob (a){
  return a + 100;
}

// Arrow Function
let bob = a => a + 100;
```

## IIFE

An IIFE (Immediately Invoked Function Expression) is a JavaScript function that runs as soon as it is defined.

```Javascript
let result = (function () {
    var name = "Barry"; 
    return name; 
})(); 
// Immediately creates the output: 
result; // "Barry"
```