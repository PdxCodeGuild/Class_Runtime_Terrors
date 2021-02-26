

const urlList = [
    'https://github.com/PdxCodeGuild/Class_Runtime_Terrors/tree/master/3%20JavaScript/docs',
    'https://github.com/PdxCodeGuild/Class_Runtime_Terrors/tree/master/3%20JavaScript/labs',
    'https://github.com/PdxCodeGuild/Class_Runtime_Terrors/blob/master/3%20JavaScript/labs/lab03_random_redirector.md'

]; 
let b = urlList.length;

window.location = urlList[random(b)];

function random(x) {
    let a = Math.floor(Math.random()*x);
    return a
}
