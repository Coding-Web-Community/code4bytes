var myArgs = process.argv.slice(2);

s = myArgs[0]
t = myArgs[1]

ag=(s,t)=>JSON.stringify(s.split('').sort((a, b) => a.localeCompare(b)))==JSON.stringify(t.split('').sort((a, b) => a.localeCompare(b)))

console.log(ag(s,t))
