//Written by EmotionIce

const request = require('request');
const util = require('util');

let numbersArray = [];
var j = 10;
for (var i = 0; i < 10; i++) {
  setTimeout(() => {
    j--;
    console.log(j);
    request('http://codingweb.eu-central-1.elasticbeanstalk.com/EmotionIce', { json: false }, (err, res, body) => {
      if (err) { return console.log(err); }
      let newNumbersArray = JSON.parse(body); //Converting the body to an array
      numbersArray = numbersArray.concat(newNumbersArray);
    });
    if(j === 0) {
        let arrAvg = arr => arr.reduce((a,b) => a + parseInt(b), 0) / arr.length;
        console.log("mean = ", arrAvg(numbersArray));

        let sdd = arr => arr.reduce((a, b) => a + Math.pow((parseInt(b) - arrAvg(numbersArray)), 2), 0) / arr.length;
        console.log("Standard Deviation = ", Math.sqrt(sdd(numbersArray)));
    }
  }, i * 600);
}
