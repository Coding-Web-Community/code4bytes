// Written by TrizlyBear#7066
// 01/29/2020

var fib = [1,2]
var c = 1
while(fib[c] + fib[c-1] < 4000000){
  var newo = fib[c] + fib[c-1]
  var old = fib
  fib.push(newo)
  
  // console.log(fib)
  if(newo + old[c] > 4000000){
    var e = 0
    var count = 0
    fib.forEach(el => {
      if(el % 2 == 0){
      e = e + el
      }
      count++
      if(count == fib.length){
      console.log(e)
      process.exit()
      }
      })
  }
  c++; 
}
