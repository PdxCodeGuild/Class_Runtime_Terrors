var redirect = [
    'https://www.google.com/',
    'https://www.allrecipes.com/recipes/17562/dinner/',
    'https://www.amazon.com/',
    'https://store.steampowered.com/',
    'https://www.java.com/en/download/',
    'http://loli.dance/'
    ]

function clickable(){
    while (true){
        let x = Math.floor(Math.random() * redirect.length)
        console.log(x)
        if (!(redirect[x] === window.location.href)){
            window.location.href = redirect[x]
            break
        }
    }
}