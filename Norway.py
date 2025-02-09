from random import *


important_crafts = {"bø":"bucket", "rø":"bread", "rr":"ingots", "rn":"axe & ingot", "8":"iron axe / pick(nh for only iron pick possible less junk)", "2":"wood tools(axe pick sword)", "lr":"garrots", "lh":"golden helmet + pick", "li":"beds or anchors (no polished blackcstone bricks)", "sa":"beds or anchors (polished blackstone bricks)", "n ":"bed, (no junk for blaze bed)"}
important_crafts_reversed = dict((v, k) for k, v in important_crafts.items())

# !!-!! for either mb or øs answer --!-- for either pl or lep answer
niche_crafts = {"er":"eyes & powder", "eb":"boat", "rø":"eyes + crossbow", "mb-øs": "junkless crossbow", "ld":"shield", "nø":"iron / stone axe", "gi":"iron bars", "nu":"tripwire hooks", "bu":"bow", "pl-lep":"gapple", "nt":"TNT"}
niche_crafts_reversed = dict((v, k) for k, v in niche_crafts.items())


inventory_crafts = {"h":"wool+bricks", "lø":"glowstone, gold axe", "gl":"glowstone / bricks", "rd":"coarse dirt", "nn":"sticks"}
inventory_crafts_reversed = dict((v, k) for k, v in inventory_crafts.items())

all_crafts_reversed = {}
for i in important_crafts_reversed:
    all_crafts_reversed[i] = important_crafts_reversed[i]
for i in niche_crafts_reversed:
    all_crafts_reversed[i] = niche_crafts_reversed[i]
for i in inventory_crafts_reversed:
    all_crafts_reversed[i] = inventory_crafts_reversed[i]

all_crafts = []

for i in important_crafts_reversed:
    all_crafts.append(i)
    all_crafts.append(i)
    all_crafts.append(i)
    all_crafts.append(i)


for i in niche_crafts_reversed:
    all_crafts.append(i)
    all_crafts.append(i)


for i in inventory_crafts_reversed:
    all_crafts.append(i)

def question():
    thing = choice(all_crafts)
    answer = input(f"what do you type when you craft {thing}? ")
    if answer == "mb" or answer == "øs":
        answer = "mb-øs"
    if answer == "pl" or answer == "lep":
        answer = "pl-lep"
    if thing in important_crafts_reversed:
        if answer == important_crafts_reversed[thing]:
            print("correct")
            return
        else:
            print("incorrect")
            print(f"correct answer: {important_crafts_reversed[thing]}")
            return
    elif thing in niche_crafts_reversed:
        if answer == niche_crafts_reversed[thing]:
            print("correct")
            return
        else:
            print("incorrect")
            print(f"correct answer: {niche_crafts_reversed[thing]}")
            return
    elif thing in inventory_crafts_reversed:
        if answer == inventory_crafts_reversed[thing]:
            print("correct")
            return
        else:
            print("incorrect")
            print(f"correct answer: {inventory_crafts_reversed[thing]}")
            return
    else:
        print("incorrect")
        print(f"correct answer: {all_crafts_reversed[thing]}")
        return



while True:
    question()