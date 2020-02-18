allowed = "abcdefghijklmnopqrstuvw"
def replace(word):
	nc = ""
	for char in word.lower():
		if char in allowed:
			nc += char
	
	return nc

words = []

with open("steve.txt", "r") as r:
	for line in r:
		for word in line.split(" "):
			if(" " in word or "\n" in word):
				pass
			else:
				words.append(replace(word))


first_nums = [0]*15
first_words = [""]*15

word_char = {}
for word in words:
	if word in word_char:
		word_char[word] += 1
	else:
		word_char[word] = 1

for word in words:
	for i in range(len(first_words)):
		if word_char[word] > first_nums[i] and word not in first_words:
			first_nums.insert(i, word_char[word])
			first_words.insert(i, word)
			del first_nums[15]
			del first_words[15]			
print(first_words)
print(first_nums)
