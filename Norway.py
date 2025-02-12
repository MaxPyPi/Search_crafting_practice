from random import *
import time

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

def question(previous_thing):
    thing = choice(all_crafts_weighted)
    while(previous_thing == thing):
        thing = choice(all_crafts_weighted)
    attempts = 1
    start_time = time.time()
    while True:
        answer = input(f"what do you type when you craft {thing}? ")
        if answer == "mb" or answer == "øs":
            answer = "mb-øs"
        if answer == "pl" or answer == "lep":
            answer = "pl-lep"
        if thing in all_crafts and answer == all_crafts[thing]:
            elapsed_time = time.time() - start_time
            print(f"correct in {attempts} attempt(s) and {round(elapsed_time, 2)} seconds")
            break
        elif attempts == 3:
            print(f"correct answer: {all_crafts[thing]}")
        attempts += 1
        print("try again")
    return thing

previous_thing = None
while True:
    previous_thing = question(previous_thing)
