//written by trizlybear

var m = [9, 8, 8, 7, 9, 8, 10, 9, 11, 10, 10, 9, 9, 8, 10, 7, 11, 8, 12, 9, 11, 10, 10, 9, 9, 8, 8, 9, 7, 8, 6]
var res = []
m.forEach((e, i, ar) => {
  if(e>m[i-1] && e>m[i+1]){
    res.push(i)
  }
})
console.log(res)
