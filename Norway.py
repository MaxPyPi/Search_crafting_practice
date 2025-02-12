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
    "boat": "eb",
    "shield": "ld",
    "iron / stone axe": "nø",
    "iron bars": "gi",
    "bow": "bu",
    "gapple": "pl-lep",
    "TNT": "nt"
}

inventory_crafts = {
    "eyes & powder": "er",
    "wool+bricks": "h",
    "glowstone, gold axe": "lø",
    "glowstone / bricks": "gl",
    "coarse dirt": "rd",
    "sticks": "nn"
}

all_crafts = {
    **important_crafts,
    **niche_crafts,
    **inventory_crafts
}

all_crafts_weighted = []
for i in important_crafts:
    all_crafts_weighted.extend([i] * 3)
for i in niche_crafts:
    all_crafts_weighted.append(i)
for i in inventory_crafts:
    all_crafts_weighted.extend([i] * 3)

def getHotkey():
    while True:
        chat_hotkey = input("What is your chat hotkey? (just enter not to use one) ")
        if(len(chat_hotkey) > 1):
            print("Not a valid hotkey")
        else:
            return chat_hotkey

def question(chat_hotkey, previous_thing):
    thing = choice(all_crafts_weighted)
    while(previous_thing == thing):
        thing = choice(all_crafts_weighted)
    attempts = 1
    start_time = time.time()
    while True:
        answer = input(f"what do you type when you craft {thing}? ")
        chat_hotkey_index = answer.find(chat_hotkey)
        if chat_hotkey_index != -1:
            if answer == "mb" or answer == "øs":
                answer = "mb-øs"
            if answer == "pl" or answer == "lep":
                answer = "pl-lep"
            if thing in all_crafts and answer[chat_hotkey_index + 1::] == all_crafts[thing]:
                elapsed_time = time.time() - start_time
                print(f"correct in {attempts} attempt(s) and {round(elapsed_time, 2)} seconds")
                break
            elif attempts == 3:
                print(f"correct answer: {all_crafts[thing]}")
            attempts += 1
            print("try again")
        else:
            print("You never used your chat hotkey...")
    return thing

previous_thing = None
chat_hotkey = getHotkey()
while True:
    previous_thing = question(chat_hotkey, previous_thing)
