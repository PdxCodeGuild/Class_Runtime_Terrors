## This

What is *this* in Javascript? This references the object that is executing the current function.

If the function is part of an object, then the function is a method. Therefore, *this* (inside the function) references the object itself.

If the function isn't part of an object, then *this* references the global object, which is the *window* object in browsers, and *global* in Node.


## First Scenario - the function is part of an object

```javascript
const video = {
     title: 'a',
     return_obj: function() {
            console.log(this)
     }
}
//it will print out the entire object
video.return_obj()
```

## Second Scenario - the function isn't part of an object

```javascript
function test(){
    console.log(this)
}
test()
```
