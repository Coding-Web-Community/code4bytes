const arr1 = process.argv[2].split("");
const arr2 = process.argv[3].split("");

const sort1 = arr1.sort();
const sort2 = arr2.sort();

console.log(sort1.join("")==sort2.join(""));
