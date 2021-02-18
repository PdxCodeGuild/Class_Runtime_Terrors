const dictionary = {feet: .3048,

    mile : 1609.34,

    kilometer : 1000

}



let unit =  prompt ('Enter the unit of measurement you want to convert into meters ');
let amount =  prompt('Enter the number of units you want to convert into meters ') ;

if (unit in dictionary && unit === 'feet'){
var dakine = Object.values(dictionary)[0];
var dakine = dakine * amount
console.log(`${amount} ${unit} equals ${dakine} meters`)
}
else if (unit in dictionary && unit === 'mile'){
var dakine = Object.values(dictionary)[1];
var dakine = dakine * amount
console.log(`${amount} ${unit} equals ${dakine} meters`)
}

else if (unit in dictionary && unit === 'kilometer'){
var dakine = Object.values(dictionary)[2];
var dakine = dakine * amount
console.log(`${amount} ${unit} equals ${dakine} meters`)
}
else{
console.log('that is not a correct entry')

const lotto_array = []
const user_array = []

i=0
while (i < 2){
  let lotto = Math.floor(Math.random()* 3)
  lotto_array.push(lotto)
  lotto_array.join()
  i++
  // console.log(array)
}

l = 0
while (l < 2){
  let lotto = Math.floor(Math.random() * 3)
  user_array.push(lotto)
  user_array.join()
  l++
  // console.log(array)
  
}

console.log(lotto_array)
console.log(user_array)

points = 0

if (lotto_array[0] === user_array[0]){
  points +=1
}
else if (lotto_array[1] === user_array[1]){
  points +=1
}
// else if (lotto_array[2] === user_array[2]){
//   points +=1
// }
// else if (lotto_array[3] === user_array[3]){
//   points +=1
// }
// else if (lotto_array[4] === user_array[4]){
//   points +=1
// }
// else if (lotto_array[5] === user_array[5]){
//   points +=1
// }
// else if (lotto_array[6] === user_array[6]){
//   points +=1
// }

let dictionary = {0:0, 1:4, 2:50}
console.log(`you won this much money : ${dictionary[points]} dollars`)


console.log(`you have this many points: ${points}`)
