console.log("Welcome to the world");

var limit = 50000;
var y = 100;    
var data = [];
var dataSeries = { type: "line" };
var dataPoints = [];
for (var i = 0; i < limit; i += 1) {
	y += Math.round(Math.random() * 10 - 5);
	dataPoints.push({
		x: i,
		y: y
	});
}
dataSeries.dataPoints = dataPoints;
data.push(dataSeries);

console.log(data)
console.log("")

