with open("coding_web_weekly_magazine.txt", "r") as f:
    text=f.read()
    f.close()
di = {}
for k in text:
    if k == " " or k == "\n": continue
    di[k] = 1 if k not in di else di[k] + 1
di2 = {}
with open("ransom_note.txt", "r") as f:
    text = f.read()
    f.close()
for k in text:
    if k == " " or k == "\n": continue
    di2[k] = 1 if k not in di2 else di2[k] + 1
pos = True
for each in di2:
    if each not in di:
        pos = False
        print("Need ", di2[each], "more", each)
        continue
    if di2[each] > di[each]:
        pos = False
        print("Need ", di2[each] - di[each], "more", each)
if pos:
    print("possible")
