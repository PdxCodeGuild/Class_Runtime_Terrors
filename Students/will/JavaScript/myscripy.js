if (2 < 10) {
    var x = 10; // scope extends beyond the if
    let y = 11; // scope is limited to the if
}
console.log(x); // 10
console.log(y); // error

for (var x=0; x<10; ++x) {}
alert(x); // 10

for (let y=0; y<10; ++i) {}
alert(y); // error