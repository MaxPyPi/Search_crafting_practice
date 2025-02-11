from random import *

important_crafts = {
    "bucket": "bø",
    "bread": "rø",
    "ingots": "rr",
    "axe & ingot": "rn",
    "iron axe / pick(nh for only iron pick possible less junk)": "8",
    "wood tools(axe pick sword)": "2",
    "garrots": "lr",
    "golden helmet + pick": "lh",
    "beds or anchors (no polished blackcstone bricks)": "li",
    "beds or anchors (polished blackstone bricks)": "sa",
    "bed, (no junk for blaze bed)": "n"
}

niche_crafts = {
    "eyes & powder": "er",
    "boat": "eb",
    "eyes + crossbow": "rø",
    "junkless crossbow": "mb-øs",
    "shield": "ld",
    "iron / stone axe": "nø",
    "iron bars": "gi",
    "tripwire hooks": "nu",
    "bow": "bu",
    "gapple": "pl-lep",
    "TNT": "nt"
}

inventory_crafts = {
    "wool+bricks": "h",
    "glowstone, gold axe": "lø",
    "glowstone / bricks": "gl",
    "coarse dirt": "rd",
    "sticks": "nn"
}

all_crafts = {
    **important_crafts_reversed,
    **niche_crafts_reversed,
    **inventory_crafts_reversed
}

all_crafts_weighted = []
for i in important_crafts_reversed:
    all_crafts.extend([i] * 4)
for i in niche_crafts_reversed:
    all_crafts.append(i)
for i in inventory_crafts_reversed:
    all_crafts.extend([i] * 3)

def question():
    thing = choice(all_crafts_weighted)
    answer = input(f"what do you type when you craft {thing}? ")
    if answer == "mb" or answer == "øs":
        answer = "mb-øs"
    if answer == "pl" or answer == "lep":
        answer = "pl-lep"
    if thing in all_crafts and answer == all_crafts[thing]: #can do this because it doesn't consider second if first is false
        print("correct")
        return
    else:
        print("incorrect")
        print(f"correct answer: {all_crafts[thing]}")
        return

while True:
    question()
