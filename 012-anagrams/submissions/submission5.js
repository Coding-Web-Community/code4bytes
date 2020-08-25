const word1 = process.argv[2];
const word2 = process.argv[3];

var charsToUse = word1.split('');

for (let char of word2) {
    var i = charsToUse.indexOf(char)
    if (i == -1) {
        console.log("False")
        process.exit(0);
    }
    charsToUse.splice(i, 1);
}

if (charsToUse.length == 0) console.log("True")
else console.log("False")
