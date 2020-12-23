# Map, Sort, Filter, Reduce. 

These are functions that you can use on arrays. They receive other functions as arguments therefore are higher order functions.

## Map

```javascript
let vals = [1, 2, 3, 4, 5];

function doublers(x) {
  return x * x;
}
let newVals = vals.map(doublers);
console.log(vals);
```

It can also be written as such:

```javascript
let vals = [1, 2, 3, 4, 5];

let newVals = vals.map(function doublers(x) {
  return x * x;
});

console.log(vals);
```

We can convert it into an arrow function:

```javascript
let newVals = vals.map((x) => x * x);
```

## Filter

```javascript
const companies = [
  { name: "Company One", category: "Finance", start: 1981, end: 2004 },
  { name: "Company Two", category: "Retail", start: 1992, end: 2008 },
  { name: "Company Three", category: "Auto", start: 1999, end: 2007 },
  { name: "Company Four", category: "Retail", start: 1989, end: 2010 },
  { name: "Company Five", category: "Technology", start: 2009, end: 2014 },
  { name: "Company Six", category: "Finance", start: 1987, end: 2010 },
  { name: "Company Seven", category: "Auto", start: 1986, end: 1996 },
  { name: "Company Eight", category: "Technology", start: 2011, end: 2016 },
  { name: "Company Nine", category: "Retail", start: 1981, end: 1989 },
];

const ages = [33, 12, 20, 16, 5, 54, 21, 44, 61, 13, 15, 45, 25, 64, 32];
```

This would be one old fashioned way to filter numbers higher than 21:

```javascript
let canDrink = [];
for (let i = 0; i < ages.length; i++) {
  if (ages[i] >= 21) {
    canDrink.push(ages[i]);
  }
}
```

We can optimize the code with _filter_:

```javascript
const canDrink = ages.filter(function (age) {
  if (age >= 21) {
    return true;
  }
});
```

It can also become an arrow function:

```javascript
const canDrink = ages.filter((age) => age >= 21);
```

```javascript
/// longer solution
const retailCompanies = companies.filter(function (company) {
  if (company.category === "Retail") {
    return true;
  }
});

//short arrow function solution
const retailCompanies = companies.filter(
  (company) => company.category === "Retail"
);

// Get 80s companies

const eightiesCompanies = companies.filter(
  (company) => company.start >= 1980 && company.start < 1990
);
```

## Sort

```javascript
const sortedCompanies = companies.sort(function (c1, c2) {
  if (c1.start > c2.start) {
    return 1;
  } else {
    return -1;
  }
});
```

Refactored into an arrow function

```javascript
const sortedCompanies = companies.sort((a, b) => (a.start > b.start ? 1 : -1));
```

## Reduce

Let's sum all the ages without _reduce_:

```javascript
let total = 0;
for (let i = 0; i < ages.length; i++) {
  total += ages[i];
}
```

With _reduce_

```javascript
const totalYears = ages.reduce(function (total, age) {
  return total + age;
}, 0);
console.log(totalYears);
```

Into an arrow function

```javascript
const totalYears = ages.reduce((total, age) => total + age , 0);

```

Let's use them all together!

```javascript
const combined = ages
  .map(age => age * 2)
  .filter(age => age >= 40)
  .sort((a, b) => a - b)
  .reduce((a, b) => a + b, 0);

console.log(combined);
```