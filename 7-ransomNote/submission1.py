import re
with open("coding_web_weekly_magazine.txt") as magazine:
    magazine = magazine.read()
with open("ransom_note.txt") as randsom:
    randsom = randsom.read()
def stringInString(magazine, randsom):
    magazine = list(re.sub(r"\s","", magazine))
    randsom = list(re.sub(r"\s","", randsom))
    badLetters = []
    for x in randsom:
        try:
            magazine.remove(x)
        except:
            badLetters.append(x)
    if badLetters:
        return badLetters
    else:
        return False
print(stringInString(magazine, randsom))
