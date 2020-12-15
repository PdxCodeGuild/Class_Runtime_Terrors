
# Events

An event can be something the browser does, or something a user does. Event handlers can be used to handle, verify user input, user actions, and browser actions: 

- Things that should be done every time a page loads
- Things that should be done when the page is closed
- Action that should be performed when a user clicks a button
- Content that should be verified when a user inputs data
- And more ...

You can read more about events on the [MDN](https://developer.mozilla.org/en-US/docs/Web/Events).


## Event Target

The target property of the Event interface is a reference to the object onto which the event was dispatched. The *event.target* property can be used in order to implement event delegation.

```html
<body>
    <ul id= 'my-list'>
        <li>rain</li>
        <li>snow</li>
        <li>sun</li>
    </ul>
<script>
    function hide(event) {
        event.target.style.visibility = 'hidden';
        console.log(event.target, event.target.tagName)
    }
    let list = document.querySelector('#my-list');
    list.addEventListener('click', hide);
</script>
</body>

```

## Defining Events

The easiest (but worst) way to define an event is inside the attribute of a tag. You do not want to have pieces of JavaScript executing in different parts of your page, it'll quickly become overwhelmingly complicated.

```html
<button id="bt" onclick="alert('hello world!');">click</button>
```

A much better way is to assign the event attribute as a function in your script tag.

```html
<button id="bt">click</button>
<script>
    let bt = document.querySelector('#bt');
    bt.onclick = function() {
        alert('hello world!');
    }
</script>
```

A third way is to use **listeners**. You can have multiple listeners for a single event, which is not possible when assigning a function directly to an attribute. You can read more about listeners on the [MDN](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener).

```html
<button id="bt">click</button>
<script>
    let bt = document.querySelector('#bt');
    bt.addEventListener('click', function() {
        alert('hello world!');
    });
</script>
```
## The Event

An HTML event can be something the browser does, or something a user does.

The target property returns the element that triggered the event, and not necessarily the eventlistener's element.

## Event Propagation

You can see an example of event propagation on [javascript.info](https://javascript.info/bubbling-and-capturing) and [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Examples#Example_5:_Event_Propagation). This [site](https://javascript.info/bubbling-and-capturing) has a good example of event bubbling.


- `event.stopPropagation()` prevents parent elements from receiving the event
- `event.stopImmediatePropagation()` prevents other listeners from receiving the event
- `event.preventDefault()` prevents an event from triggering


## List of Events

You can find a comprehensive list of events on the [MDN](https://developer.mozilla.org/en-US/docs/Web/Events).


| Event | Triggered when... |
|--- |--- |
| `load` | an element is loaded |
| `focus` | an element gains focus |
| `blur ` | element loses focus |
| `input` | the user inputs a value |
| `change` | an input's value is changed |
| `keydown` | any key is pressed |
| `keyup` | any key is released |
| `keypress` | any button except Shift, Fn, CapsLock is pressed (fires continuously) |
| `click` | the mouse has been pressed and released |
| `mousedown` | the mouse has been pressed |
| `mouseup` | the mouse has been released |
| `mouseenter` | the mouse has entered the element |
| `mouseleave` | the mouse has exited the element
| `mousemove` | the mouse has moved on the element |


### `load` and `unload`


```javascript
window.onload = function() {
    // here it's safe to access DOM elements
    // because everything on the page has been loaded
}
```

The `beforeunload` event is called immediately before an element is unloaded. This can be used on the window to ask whether the use wants to leave a page without saving their data.

```javascript
window.onbeforeunload = function(){
  return 'Are you sure you want to leave?';
};
```

### `input` and `change`

The `input` and `change` events can be used with `input` elements to detect when the user changes a value. The `input` event is triggered whenever a letter is entered. The `change` event is triggered when the element loses focus and the value has been changed.

```html
<input id="user_input" type="text"/>
<script>
    let user_input = document.getElementById('user_input');
    user_input.oninput = function() {
        console.log('user entered some text: '+user_input.value);
    };
    user_input.onchange = function() {
        console.log('user changed value: '+user_input.value);
    }
</script>

```

### Keyboard Events

You can view a list of keycodes on [css-tricks.com](https://css-tricks.com/snippets/javascript/javascript-keycodes/).

| Event | Triggered when... |
|--- |--- |
| `keydown` | any key is pressed |
| `keyup` | any key is released |
| `keypress` | any button except Shift, Fn, CapsLock is pressed (fires continuously) |


```html
<script>
    document.body.onkeydown = function(evt) {
      alert(evt.keyCode);
    }
</script>
```

### Mouse Events

| Event | Triggered when... |
|--- |--- |
| `click` | the mouse has been pressed and released |
| `mousedown` | the mouse has been pressed |
| `mouseup` | the mouse has been released |
| `mouseenter` | the mouse has entered the element |
| `mouseleave` | the mouse has exited the element
| `mousemove` | the mouse has moved on the element |

```html
<body>
  <div id='container'></div>
   <style>
   #container{
    width: 200px;
    height: 200px;
    background: red;
   }
   </style> 
    <script>
    let container = document.querySelector('#container')
    container.addEventListener('mouseenter', function(event){
        if (event.target.style.backgroundColor == 'blue'){
            event.target.style.backgroundColor = 'red'
        } else {
            event.target.style.backgroundColor = 'blue'
        }
    })
    </script>
</body>

```

### Determining the Mouse's Position

The event parameter that's passed to the function contains the coordinates of the mouse, and which button is pressed.

```html
<canvas id="cnv" width="100" height="100"></canvas>
<script>
let cnv = document.getElementById('cnv');
cnv.onclick = function(event) {
    var x = event.clientX;
    var y = event.clientY;
    alert('position: '+x+', '+y);
}
</script>
```

### Handling Dragging

To handle dragging, you can just set a boolean variable `mouse_down` to `true` when the mouse is pressed, and `false` when the mouse is released or exits. Then within the `mousemove` event, you can check if the mouse is down or not.


