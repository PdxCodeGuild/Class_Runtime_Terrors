let urls = []

urls[0] = "https://pdxcodeguild.com/"
urls[1] = "https://github.com/PdxCodeGuild/Class_RunCount_Terrors/blob/master/1%20Python/docs/01%20-%20Overview.md"
urls[2] = "https://github.com/PdxCodeGuild/Class_Runtime_Terrors/blob/master/2%20HTML%20%2B%20CSS/docs/01%20-%20HTML%20Overview.md"
urls[3] = "https://github.com/PdxCodeGuild/Class_Runtime_Terrors/blob/master/3%20JavaScript/docs/00%20-%20JavaScript%20Overview.md"
urls[4] = "https://github.com/PdxCodeGuild/Class_Runtime_Terrors/blob/master/Django/1_django_steps_getting_started.md"

console.log(urls)
function getRandomInt() {
    return Math.floor(Math.random() * Math.floor(5));
}
function timing() {
    setTimeout(runCount1, 1000)
    setTimeout(runCount2, 2000)
    setTimeout(runCount3, 3000)
    setTimeout(runCount4, 4000)
    setTimeout(runCount5, 5000)
    setTimeout(myRedirect, 6000)
}
let call = timing()
function runCount1() {
    console.log("")
    document.getElementById("redir").innerHTML = " > 5️⃣ Get Ready.";
}
function runCount2() {
    console.log("")
    document.getElementById("redir").innerHTML = " >> 4️⃣ Ignition Start.";
}
function runCount3() {
    console.log("")
    document.getElementById("redir").innerHTML = " >>> 3️⃣ Throttle Up.";
}
function runCount4() {
    console.log("")
    document.getElementById("redir").innerHTML = " >>>> 2️⃣ Launch";
}
function runCount5() {
    console.log("")
    document.getElementById("redir").innerHTML = " >>>>> 1️⃣ BLAST OFF!";
}
function myRedirect() {
    let someNum = getRandomInt()
    console.log(someNum)
    if (someNum >= 0 || someNum <= 4) {
        location = urls[someNum]
    }
}