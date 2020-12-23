// //ver1 
// const myHeaders = new Headers();
// const url = 'https://favqs.com/api/qotd';
// myHeaders.append('Authorization',  'Token token="  83ff6c5e1850ac35856e1869206dd66e"');
// let outputter = document.getElementById('outputter')

// function dakine(){
// fetch(url, {
//   method: 'GET',
//   headers: myHeaders,
// })
//  .then(function(response){
//     return response.json()
//   })
//  .then(function(data){
//     //or pass a callback function to handle data
//     console.log(data) 
//     console.log(data.quote.body)  
//     outputter.innerHTML = data.quote.body    
// })
//   .catch(function(error){
//     console.error('There has been a problem with your fetch operation:', error);
//   });
// }

//ver2     
// const myHeaders = new Headers();
// myHeaders.append('Authorization', 'Token token="83ff6c5e1850ac35856e1869206dd66e"');

// function dakine (){
//     let filter = document.getElementById("filter").value;
//     let outputter = document.getElementById("outputter");
//     if (filter.length !== 0){
//         console.log('good to go')
//         fetch(`https://favqs.com/api/quotes?page=1&filter=${filter}`, {
//         method: 'GET',
//         headers: myHeaders,
//         })
//         .then(function(response){
//             return response.json()
//         })
//         .then(function(data){
//             console.log(data);
//             for (let i = 0; i< 25; i++) {
//             outputter.innerText+=(data.quotes[i].body) 
//             }
//         })
//         .catch(function(error){
//             console.error('There has been a problem with your fetch operation:', error);
//         });
//     }
// }

//ver 2 making added DOM elements into a nice list 
const myHeaders = new Headers();
myHeaders.append('Authorization', 'Token token="83ff6c5e1850ac35856e1869206dd66e"');

function dakine (){
    let filter = document.getElementById("filter").value;
    let list = document.getElementById("list");
    if (list.hasChildNodes){
        list.innerText = '';
    }
    if (filter.length !== 0){
        console.log('good to go')
        fetch(`https://favqs.com/api/quotes?page=1&filter=${filter}`, {
        method: 'GET',
        headers: myHeaders,
        })
        .then(function(response){
            return response.json()
        })
        .then(function(data){
            console.log(data);
            for (let i = 0; i< 25; i++) {
                let item = document.createElement('li');
                item.innerText+=(data.quotes[i].body) 
                list.appendChild(item)
            }
        })
        .catch(function(error){
            list.innerText = 'no quotes found'
            console.error('There has been a problem with your fetch operation:', error);
        });
    } else {
        const url = 'https://favqs.com/api/qotd';
        fetch(url, {
        method: 'GET',
        headers: myHeaders,
        })
        .then(function(response){
            return response.json()
        })
        .then(function(data){
            //or pass a callback function to handle data
            console.log(data) 
            console.log(data.quote.body)  
            list.innerHTML = data.quote.body    
        })
        .catch(function(error){
            console.error('There has been a problem with your fetch operation:', error);
        });

    }
}

