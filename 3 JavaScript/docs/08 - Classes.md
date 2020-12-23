
# Classes

## Introductory Example

ES6 introduced a much easier way of writing classes. Below is an example comparing the use of a class to that of an object. The object behaves similarly, except you'll have to re-write the entire structure every time you create an instance. Also, each instance will have its own copy of the `getBalance` function, resulting in greater memory overhead. 

```javascript
// using a class
class Atm {
    constructor(balance=0) {
      this.balance = balance;
    }
    getBalance() {
      return this.balance;
    }
}

let wellsFargo = new Atm();
console.log(wellsFargo.get_balance());

// using an object
let atm = {
  balance: 5.0,
  getBalance: function() {
    return this.balance;
  }
};

console.log(atm.getBalance())
```

## Inheritance

```javascript
class Animal {
    constructor(legs = 0) {
        this.legs = legs;
    }

    move() {
        if (this.legs > 0) {
            console.log('walk');
        } else {
            console.log('slither');
        }
    }
}

class Dog extends Animal {
    constructor(legs = 4, sound = 'ruff') {
        super(legs); // invoke the parent class's constructor
        this.sound = sound;
    }

    bark() {
        console.log(this.sound);
    }
    
    move() { // override the parent method
      super.move(); // call the parent method (optional)
      console.log('dog moving');
    }
}

let myDog = new Dog(4);

console.log(myDog.legs); // logs 4
myDog.move(); // logs 'walk', 'dog moving'
myDog.bark(); // logs 'ruff'
```

The way to do classes is ES5 is much more awkward, but you may see it in the wild, so it's worth knowing.

```javascript
function Animal(legs) {
    this.legs = legs || 0; // use default value if needed
}

Animal.prototype.move = function () {
    if (this.legs > 0) {
        console.log('walk');
    } else {
        console.log('slither');
    }
};

function Dog(legs, sound) {
    Animal.call(this, legs); // parent 'constructor'
    this.sound = sound || 'ruff';
}

Dog.prototype = Object.create(Animal.prototype);

Dog.prototype.bark = function () {
    console.log(this.sound);
};

var myDog = new Dog(4);

console.log(myDog.legs); // logs 4
myDog.move(); // logs 'walk'
myDog.bark(); // logs 'ruff'
```

Functions and classes are objects. Functions inherit from the Object prototype and they can be assigned key: value pairs. These pairs are referred to as *properties* and can themselves be functions (i.e., *methods*).

The most important thing to remember is that classes are just normal JavaScript functions and could be completely replicated without using the class syntax. It is special syntactic sugar added in ES6 to make it easier to declare and inherit complex objects. Let's see an example:

```javascript
function createNewPerson(name) {
  const obj = {};
  obj.name = name;
  obj.greeting = function() {
    console.log('Hi! I\'m ' + obj.name + '.');
  };
  return obj;
}
const john = createNewPerson('John');
john.name;
john.greeting();
```

To simplify, the same can be written as the following:

```javascript
function Person(name) {
  this.name = name;
  this.greeting = function() {
    console.log('Hi! I\'m ' + this.name + '.');
  };
}

let person1 = new Person('Bob');
console.log(person1.greeting())

```

Here's how inheritance looks like using functions:

```javascript
function Brick() {
  this.width = 10;
  this.height = 20;
}

function BlueGlassBrick() {
  Brick.call(this);

  this.opacity = 0.5;
  this.color = 'blue';
}

let shape = new BlueGlassBrick()

console.log(shape.width)

```