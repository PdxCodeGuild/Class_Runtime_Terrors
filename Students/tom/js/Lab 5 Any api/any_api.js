let getData = document.getElementById('getData') //search button
let dataYear = document.getElementById('dataYear') // filter input box
let selectedState = document.getElementById('state') //drop down
const myHeaders = new Headers()

getData.addEventListener('click', function(){
  let url = `https://datausa.io/api/data?drilldowns=State&measures=Population&year=${dataYear.value}`
  
  fetch(url, {
    method: 'GET',
  })
  .then(function(response){
    return response.json()
  })  
  .then(function(data){
    console.log('parsed json: ', data) //Parsed Data
    census_data = data
    processData()
  })       
  .catch(function(error){
    console.error('There has been a problem with your fetch operation:', error);
  })
})

function processData(){
  let totalPopulation = 0
  for (i in census_data.data){
    totalPopulation += census_data.data[i].Population //Sums all populations
    if (census_data.data[i].State == selectedState.value){
      stateNumber = i
    }
  }
  
  averagePopulation = (totalPopulation / i).toFixed() //Averages state populations
  
  selectedStatePopulation = (census_data.data[stateNumber].Population) //Population of state
  
  if (selectedStatePopulation > averagePopulation){ //Determines Greater than / Less than
    comparison = "greater than"
  } else {
    comparison = "less than"
  }
  
  stateName = census_data.data[stateNumber].State //Name of state
  
  difference = Math.abs(selectedStatePopulation - averagePopulation)
  
  selectedStatePopulation = selectedStatePopulation.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") //Population of state with commas
  document.getElementById('stateInfo').innerHTML = stateName + "'s population for the year of "+ dataYear.value + " is " + selectedStatePopulation + "."

  totalPopulation = totalPopulation.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") //Sums all populations with commas
  document.getElementById('nationalInfo').innerHTML = "The national population for the year of "+ dataYear.value + " is " + totalPopulation + "."
  
  averagePopulation = averagePopulation.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") //Averages state populations with commas
  document.getElementById('averagePopulation').innerHTML = "The average state population for the year of " + dataYear.value + " is " + averagePopulation + "."

  difference = difference.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
  document.getElementById('populationCompare').innerHTML = stateName + "'s population is " + difference + " " + comparison + " the national average."
}