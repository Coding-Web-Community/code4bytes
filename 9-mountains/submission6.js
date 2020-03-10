//Written by ...HutchyBen

var ctx = document.getElementById("canvas").getContext("2d");
function createGraph(data) {

  peakData = []
  peakPoints = []
  for (let i = 1; i < data.length; i++) {
    if (data[i] > data[i + 1] && data[i] > data[i - 1]) {
      peakData.push({x: i, y: data[i]})
      peakPoints.push(i)
    }
  }
  console.log(peakPoints)

  var chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: Array.from(data.keys()),
      datasets: [{
        label: "The Mountain",
        data: data,
        lineTension: 0,
        pointRadius: 0
      },{
        label: "Peaks",
        data: peakData,
        type: "scatter",
        pointRadius: 5,
        backgroundColor: "#ffaaaa", 
        pointBackgroundColor: "#ffaaaa"
      }]
    },
  })
}
// ARRAY OF MOUNTAIN HERE
createGraph([9, 8, 8, 7, 9, 8, 10, 9, 11, 10, 10, 9, 9, 8, 10, 7, 11, 8, 12, 9, 11, 10, 10, 9, 9, 8, 8, 9, 7, 8, 6]);
