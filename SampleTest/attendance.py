import random
from collections import OrderedDict

nl = ["Derek", "Ric", "Connie", "Wan"]
per_dict = OrderedDict()

rl = []
i = 1

while i <= len(nl):
    rl.append(i)
    i = i + 1

while len(nl) > 0:
    val = random.choice(rl)
    person = random.choice(nl)
    per_dict[val] = person
    rl.remove(val)
    nl.remove(person)

for key in sorted(per_dict.keys()):
    print(key, "->", per_dict[key])
