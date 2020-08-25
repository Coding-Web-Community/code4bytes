a = """ 01234567891abcdefghijklmnopqrstuvwxyz.,?!"""

text = []

with open("steveraw.txt", "r") as f:
	for line in f:
		nl = ""
		for char in line:
			if char.lower() in a:
				nl += char.lower()
	
		text.append(nl)

f.close()

for i in range(5):
	for j in range(len(text)):
	#	text[j] = text[j].replace("  ", " ")
		pass
for i in range(len(text)):
	text[i] += "\n"

print(len(text))
with open("steve.txt", "w") as c:
	for i in text:
		c.write(i)
