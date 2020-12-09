## How Does Javascript Work?

You can also view a short video about this lecture [here](https://www.youtube.com/watch?v=8aGhZQkoFbQ)

Javascript is a single threaded language, however it is capable of asynchronous operations. This means that an event such as an API call can be performed while other events can still computed such as a user scrolling or entering data.

Just to make some clear examples, this is synchornous code running:

```javascript
console.log(1)
console.log(2)
console.log(3)
```

This below is an example of asynchronous code that is possible thanks to the *event loop*

```javascript
console.log(1)
setTimeout(() => {
    console.log('hey!')
  }, 3000)
console.log(3)
///returns 1, 3, hey!
```
Imagine that setTimeout is an API call that takes a long time to run, and `console.log(3)` represents the ability to scroll down a web page. Because of the *event loop* and asynchronous code, we can perform other operations while lenghty code is being executed.

setTimeout is momentarily queued in a separate stack called *task queue*, that's why other code runs before it. The same happens with API calls, or other asynchronous code. It gets momentarily taken away from the stack into a separate queue, and brought back when ready by the *event loop*.

The event loop handles this with the concepts of a *stack* and a *queue*. Take a look at the following picture to understand the concept better:

<img src="https://miro.medium.com/max/2400/1*iHhUyO4DliDwa6x_cO5E3A.gif"
     alt="Javascript Event Loop"/>

## Call Stack

You should imagine the call stack like one line of bricks stacked vertically. Bricks repesent code or functions. Every time a function gets executed in JavaScript, a brick gets added to the Stack. After its execution, it is removed from the stack. Slow code can be temporarily queued in a secondary queue (*task queue*). 

How does slow code end up in a separate queue? Thanks to a callback function. Then, the queued code can be brought back to the call stack for its final execution by the event loop.

## Queue (task queue)

Whenever the call stack is empty, the event loop will check the queue for any waiting messages, starting from the oldest message. Once it finds one, it will add it to the stack, which will execute the function in the message.

## Event Loop

It keeps running continuously and checks the main stack (call stack), if it has any code to execute, if not then it checks the callback queue (task queue), if the callback queue has codes to execute then it pops the message from it to the main stack for the execution.