def make_dict(string):
	d = {}
	for char in string:
		if char not in d:
			d[char] = 1
		else:
			d[char] += 1

	return d

def ransom(ransom, magazine):
	if(len(ransom) > len(magazine)):
		return False
	
	ransom_dict, magazine_dict = make_dict(ransom), make_dict(magazine)

	for char in ransom_dict:
		if char not in magazine_dict:
			print(char, ransom_dict[char])
			return False	
		elif ransom_dict[char] > magazine_dict[char]:
			print(char, ransom_dict[char], magazine_dict[char])
			return False

	return True
		

print(ransom("aa","ab"))
print(ransom("ab","aabb"))
print(ransom("abc", "cba"))
string = "dear parents, friends and family of elemental. i am sending you this letter to inform you that he is fine. besides a couple scratches he is doing better than ever. we have given him some steroids and a bench press. he has a massive 6 pack now. if you ever wanna see him like this alive, pay us 100k in bytes asap. do not call the police or we will make him listen to country music legends such as toby keith, hank williams and dolly parton! you know damn well he doesn't like that and will most likely not survive."
mag = "coding web weekly magazine! in this episode of coding web weekly we will talk about the wonderous language of go. golang is hailed by many as the new number 1, best language on the block. it was developed by google in 2007. it was announced late 2009. with developers such as rob pike and ken thompson it could only be good. and it is! it's a staticly typed, structural language with a syntax that resembles both c++ and python. its incredible speed and strong focus on scalability made it a perfect language for building server applications such as apis and even web frameworks. it is also being used in the popular virtualization software: docker, further solidifying golang inside every server closet. if you haven't tried golang out for yourself, what are you waiting for? i will personally give you all a warm welcome in the #go channel. in other news: i can confirm the death of channels such as #security, #discord4j and #web-frameworks. further i would like to thank frog for asking if everybody needs help, what a champ! thank you again for reading coding web weekly magazine. i hope to see you next time where we will talk about how crap javascript is!"
print(ransom(string, mag))
