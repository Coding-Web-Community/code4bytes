#submission by frog

hex_to_dec=lambda hex_num: sum([(16**xi)*("0123456789ABCDEF".index(x)) for xi, x in enumerate(hex_num[::-1])])

# run function
import json
with open("tests.json") as json_file:
    data = json.loads(json_file.read())
for value in data:
    try:
        out = hex_to_dec(value['input'])
        fails = out != value['result']
    except ValueError:
        fails = True
    if fails == value['fails']:

        print('works')
    else:
        print("fails")