import os

RARITY_MULTIPLIERS = [
    8, 11, 12, 17, 20, 27, 35, 11, 11, 11, 48, 99999, 13, 16, 22, 34, 43
]

TIER_MULTIPLIERS = [
    0,  # unused
    (50, 750),
    (40, 600),
    (40, 600),
    (30, 450),
    (20, 300),
    (20, 300),
    (10, 150)
]

TIER_NAMES = [
    "Exotic",
    "Exquisite",
    "Transcendent",
    "Enigmatic",
    "Unfathomable",
    "Otherworldly",
    "Zenith"
]

def clear():
    os.system('cls') # This defines the border between win and unix!!! for some reason

def get_tier_multiplier(tier):
    if 1 <= tier <= 7:
        return TIER_MULTIPLIERS[tier]
    else:
        return (0, 0)  # use default multipliers for invalid tiers

def get_cave_multiplier(cave):
    if cave == 18:
        print("Wow you chose gilded, did you know that gilded caves are weird? Multiplying by 2.5x")
        gilded_multiplier = 2.5
        print("Did you happen to have the 57 Leaf Clover pickaxe equipped?")
        print("1 - yes,\n2 - no")
        clover_choice = int(input())
        clear()
        if clover_choice == 1:
            print("Loser, multiplying by 57x")
            return gilded_multiplier * 57
        else:
            print("Wowie, multiplying by 5700x")
            return gilded_multiplier * 5700
    elif 1 <= cave <= 17:
        return RARITY_MULTIPLIERS[cave - 1]
    else:
        return 1  # use default multiplier for invalid caves

print("Insert ore rarity:")
rarity = int(input())
print("Insert tier:\n1 - Exotic,\n2 - Exquisite,\n3 - Transcendent,\n4 - Enigmatic,\n5 - Unfathomable,\n6 - Otherworldly,\n7 - Zenith")
tier = int(input())
print("Insert type:\n1 - Regular,\n2 - Ionized,\n3 - Spectral")
type_choice = int(input())

if type_choice != 1:
    ion_multiplier, spec_multiplier = get_tier_multiplier(tier)
    rarity *= ion_multiplier if type_choice == 2 else spec_multiplier
    clear()
    print(f"Tier multiplier: {TIER_NAMES[tier - 1]}")
    print(f"Ionized Constant: {ion_multiplier}x\nSpectral Constant: {spec_multiplier}x\n") 

print(f'{rarity:,}\n')

print("Type 1 to begin cave calculation")
cave_choice = int(input())

if cave_choice == 1:
    clear()
    rarity *= 1.88
    print("Input cave: (Multiplying by 1.88x)")
    print("---WORLD 1---")
    print("1 - Frozen\n2 - Metallic\n3 - Geode\n4 - Elemental\n5 - Divine\n6 - Prismatic\n7 - Void")
    print("---SUBWORLD 1---")
    print("8 - Magmatic\n9 - Radioactive\n10 - Interstellar\n11 - nil\n12 - feebium")
    print("---WORLD 2---")
    print("13 - Unstable\n14 - Galactic\n15 - Enchanted\n16 - Luminous\n17 - Nightfall")
    print("---SPECIAL---")
    print("18 - Gilded")
    cave_choice = int(input())
    rarity *= get_cave_multiplier(cave_choice)

print("We're done. Final rarity:")
print(f'{rarity:,}')