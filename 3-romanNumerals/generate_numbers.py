roman = ['M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

rom_to_num = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
num_to_rom = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}

def num_to_roman(n):
	result = []
	for i in range(len(roman)):
		count = int(n / num[i])
		result.append(roman[i] * count)
		n -= num[i] * count
	
	r = "".join(result)
	return r
	
def roman_to_num(r):
	count = 0
	for i in range(len(r)):
		try:
			if(rom_to_num[r[i+1]] > rom_to_num[r[i]]):
				count -= rom_to_num[r[i]]
			else:
				count += rom_to_num[r[i]]

		except:	
			count += rom_to_num[r[i]]		
	return count 

import random


for i in range(1,3999):
	x = num_to_roman(i)
	if(i != roman_to_num(x)):
		print("WOOPS {} {}".format(x, i))

with open("roman_numerals.txt", "w") as file:
	count = 0
	for i in range(100):
		x = random.randint(1,3999)
		count += x
		s = num_to_roman(x) 
		file.write(s + ",")

	print(count)
