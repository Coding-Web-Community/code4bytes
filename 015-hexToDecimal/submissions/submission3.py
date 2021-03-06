#submission by gang

import json
with open("tests.json") as f:
    cases = json.load(f)

uwu = lambda x: (lambda n: sum([int(j)*(16**i) if j.isdigit() else ((("ABCDEF".index(j)+10) * (16**i)) if j in "ABCDEF" else "lol") for i, j in enumerate(n[::-1])]) if "lol" not in [int(j)*(16**i) if j.isdigit() else ("ABCDEF".index(j)+11 if j in "ABCDEF" else "lol") for i, j in enumerate(n)] else 0)(list(x.lstrip('0')))


for case in cases:
    output = uwu(case["input"])
    if case["fails"]:
        assert output == 0

    else:
        assert output == case["result"]

print("Zero assertion errors baby. I can smell those bytes.")
