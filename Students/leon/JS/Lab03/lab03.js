let pages = []

pages[0] = "https://developer.mozilla.org/en-US/docs/Web/JavaScript"
pages[1] ="https://www.w3schools.com/jsref/met_element_remove.asp"
pages[2] = "https://howto-wordpress-tips.com/change-bullet-point-color-replace-shape-css/"
pages[3] = "https://www.geeksforgeeks.org/how-to-decorate-list-bullets-in-arrow-using-css/"
pages[4] = "https://unicode-table.com/en/#25CB"

console.log(pages)

// function getRandomInt(max) {
//     return Math.floor(Math.random() * Math.floor(max));
// }

function getRandomInt() {
    return Math.floor(Math.random() * Math.floor(5));
}


function timing() {
    setTimeout(myTimeout1, 1000)
    setTimeout(myTimeout2, 2000)
    setTimeout(myTimeout3, 3000)
    setTimeout(myTimeout4, 4000)
    setTimeout(myTimeout5, 5000)
    setTimeout(myRedirect, 6000)
    // let someNum = setTimeout(getRandomInt, 6000)
    // console.log(someNum)
    // if (someNum >= 0 || someNum <= 4) {
    //     location = pages[someNum]
    // }
}

let call = timing()

// for (i=0; i<5; i++) {
//     call = timing()
// }


function myTimeout1() {
    console.log("...checking files...")
    document.getElementById("para").innerHTML = "5 seconds...";
}

function myTimeout2() {
    console.log("...checking files...")
    document.getElementById("para").innerHTML = "4 seconds...";
}

function myTimeout3() {
    console.log("...checking files...")
    document.getElementById("para").innerHTML = "3 seconds...";
}

function myTimeout4() {
    console.log("...checking files...")
    document.getElementById("para").innerHTML = "2 seconds...";
}

function myTimeout5() {
    console.log("...checking files...")
    document.getElementById("para").innerHTML = "1 seconds...";
}

function myRedirect() {
    let someNum = getRandomInt()
    console.log(someNum)
    if (someNum >= 0 || someNum <= 4) {
        location = pages[someNum]
    }
}
// let timer = document.getElementById("para");
// timer.innerText = 5





