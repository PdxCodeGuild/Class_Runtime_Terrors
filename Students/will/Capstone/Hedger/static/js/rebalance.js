console.log('words words words')

<<<<<<< HEAD
<<<<<<< HEAD
console.log(balances)
=======
>>>>>>> 30d074996118eabf39297f0c7f6137047f4132b6
=======
>>>>>>> 4996abcf50a91e81220314bf284bb3f2054b4984
///////////////////////////////////////////////////////////    PIE CHART
var reverse = balances.length
reverse = balances[reverse-1]
reverse = reverse['fields']
var Account_value = reverse['Account_value']
var BTC_balance = reverse['BTC_balance']
var PAX_value = reverse['PAX_value']
var BTC_percentage = (BTC_balance/Account_value)*100
BTC_percentage = BTC_percentage.toFixed(2)
PAX_percentage = 100 - BTC_percentage
var chart_pie = new CanvasJS.Chart("account_pie",
{
    backgroundColor: "#e5ffdf",
    theme: "light2",
    title:{
    text: "Account Value:" + Account_value + 'BTC', 
    fontFamily: 'Roboto Mono',
    fontWeight: "normal",
    fontSize: 25
    },
    toolTip:{
    enabled: false,       //disable here
    animationEnabled: true //disable here
    },
    data: [{
    type: "pie",
    startAngle: 60,
    legendText: "{indexLabel}",
    dataPoints: [
    {  y: BTC_percentage, indexLabel: "Bitcoin "+BTC_percentage+'%', color: "#F79400" },
    {  y: PAX_percentage, indexLabel: "Gold "+PAX_percentage+'%', color: "#D0B13E" },
    ]}]
});
chart_pie.render();
<<<<<<< HEAD
<<<<<<< HEAD
//////////////////////////////////////////////////////////   BTC CHART
=======
//////////////////////////////////////////////////////////   Account CHart
>>>>>>> 30d074996118eabf39297f0c7f6137047f4132b6
=======
//////////////////////////////////////////////////////////   Account CHart
>>>>>>> 4996abcf50a91e81220314bf284bb3f2054b4984
var data = [];
var dataSeriesaccount = { type: "area" };
var dataPoints = []
for(i=0; i<balances.length;i+=2){
dataPoints.push({
    x: i, // balances[i].fields.date_time, 
    y: Number(balances[i].fields.Account_value)
});
}
dataSeriesaccount.dataPoints = dataPoints;
data.push(dataSeriesaccount);
var options = {
zoomEnabled: true,
animationEnabled: true,
backgroundColor: "#e5ffdf",
theme: "light2",


title: {
<<<<<<< HEAD
<<<<<<< HEAD
    text: "Account Balance:" + Account_value + 'BTC',
=======
    text: "Account Balance:" + Number(Account_value).toFixed(4) + ' BTC',
>>>>>>> 30d074996118eabf39297f0c7f6137047f4132b6
=======
    text: "Account Balance:" + Number(Account_value).toFixed(4) + ' BTC',
>>>>>>> 4996abcf50a91e81220314bf284bb3f2054b4984
    fontFamily: 'Roboto Mono',
},
axisY: {
    suffix: "BTC",
    lineThickness: 1
},
data: data  // random data
};
var chart_line_BTC_QTY = new CanvasJS.Chart("chart_line_BTC_QTY", options);
chart_line_BTC_QTY.render();
//////////////////////////////////////////////////////////   PAX CHART
PAX_balance = reverse['PAX_balance']
var data = [];
var dataSeriesaccount = { type: "area", color: "#D0B13E" };
var dataPoints = []
for(i=0; i<balances.length;i+=2){
dataPoints.push({
    x: i, // balances[i].fields.date_time, 
    y: Number(balances[i].fields.PAX_balance)
});
}
dataSeriesaccount.dataPoints = dataPoints;
data.push(dataSeriesaccount);

var options = {
borderThickness: 2,

zoomEnabled: true,
animationEnabled: true,
backgroundColor: "#e5ffdf",
theme: "light2",
    
    
    title: {
<<<<<<< HEAD
<<<<<<< HEAD
      text: "Total Gold Balance: " + PAX_balance + 'oz',
=======
      text: "Total Gold Balance: " + Number(PAX_balance).toFixed(4) + ' oz',
>>>>>>> 30d074996118eabf39297f0c7f6137047f4132b6
=======
      text: "Total Gold Balance: " + Number(PAX_balance).toFixed(4) + ' oz',
>>>>>>> 4996abcf50a91e81220314bf284bb3f2054b4984
      fontFamily: 'Roboto Mono',
    },
    axisY: {
      suffix: "oz",
      lineThickness: 1
    },
    data: data  // random data
  };
  var chart_line_BTC_PAX_QTY = new CanvasJS.Chart("chart_line_BTC_PAX_QTY", options);
  chart_line_BTC_PAX_QTY.render();
//////////////////////////////////////////////////////////   BTC CHART
BTC_balance = reverse['BTC_balance']
var data = [];
var dataSeriesaccount = { type: "area", color: "#F79400" };
var dataPoints = []
for(i=0; i<balances.length;i+=2){
    dataPoints.push({
    x: i, // balances[i].fields.date_time, 
    y: Number(balances[i].fields.BTC_balance)
    });
}
dataSeriesaccount.dataPoints = dataPoints;
data.push(dataSeriesaccount);

var options = {
    zoomEnabled: true,
    animationEnabled: true,
    backgroundColor: "#e5ffdf",
    theme: "light2",
        
    title: {
<<<<<<< HEAD
<<<<<<< HEAD
    text: "Total Bitcoin Balance: " + BTC_balance + 'BTC',
=======
    text: "Total Bitcoin Balance: " + Number(BTC_balance).toFixed(4) + ' BTC',
>>>>>>> 30d074996118eabf39297f0c7f6137047f4132b6
=======
    text: "Total Bitcoin Balance: " + Number(BTC_balance).toFixed(4) + ' BTC',
>>>>>>> 4996abcf50a91e81220314bf284bb3f2054b4984
    fontFamily: 'Roboto Mono',
    },
    axisY: {
    suffix: "oz",
    lineThickness: 1
    },
    data: data  // random data
};
var chart_line_BTC_BAL = new CanvasJS.Chart("chart_line_BTC_BAL", options);
chart_line_BTC_BAL.render();


<<<<<<< HEAD
<<<<<<< HEAD
for (let item in balances){
    table = document.getElementById('table_api_resonse')
    tr = document.createElement('tr')
    tr.innerHTML = balances.API_reply
    table.appendChild(tr)
    console.log('yes')
    
}
   
=======
=======
>>>>>>> 4996abcf50a91e81220314bf284bb3f2054b4984


table_items=[];
for(i=0; i<balances.length;i++){
    table_items.push({
        BTC_balance : balances[i].fields.BTC_balance, 
        PAX_value : balances[i].fields.PAX_value,
        API_reply : balances[i].fields.API_reply
    })
    };

for (i=0; i<table_items.length;i++){
    table = document.getElementById('table_api_resonse')
    var row = table.insertRow(1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    cell1.innerHTML = table_items[i].BTC_balance;
    cell2.innerHTML = table_items[i].PAX_value;
    cell3.innerHTML = table_items[i].API_reply;
}
console.log(table_items);
console.log(balances);
<<<<<<< HEAD
>>>>>>> 30d074996118eabf39297f0c7f6137047f4132b6
=======
>>>>>>> 4996abcf50a91e81220314bf284bb3f2054b4984
