import random
from collections import OrderedDict

rl = [1,2,3,4]
nl = ["Derek", "Ric", "Connie", "Wan"]
per_dict = OrderedDict()

while len(nl) > 0:
    val = random.choice(rl)
    person = random.choice(nl)
    per_dict[val] = person
    rl.remove(val)
    nl.remove(person)

for key in sorted(per_dict.keys()):
    print(key, "->", per_dict[key])
