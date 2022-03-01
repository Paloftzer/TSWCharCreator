import random
import time
import msvcrt as m

def MainMenu():
    print("","-"*72)
    print(" Hello and Welcome to the Top Strongest Wikia custom character generator!")
    print("","-"*72)
    print()
    print()
    print(" 1 - Generate a custom or random amount of Abilities")
    print()
    print(" 2 - Generate a Character's Physical Strength")
    print()
    print(" 3 - Generate a Character's Attack Potency/Destructive Capacity")
    print()
    print(" 4 - Generate a Character's Durability")
    print()
    print(" 5 - Generate a Character's Movement Speed")
    print()
    print(" 6 - Generate a Character's Reaction Speed")
    print()
    print(" 7 - Generate a Character's Intelligence")
    print()
    print(" 8 - Generate a Character's Stamina")
    print()
    print(" 9 - Generate a Character's Range")
    print()
    print(" 10 - Generate a Character's Weakness")
    print()
    print(" 11 - Generate a full Character")
    print()
    print(" 12 - Display your generated character's full information")
    print()
    print(" 13 - Clear your saved stats to make a new character")
    print()
    print(" 14 - Save your character to a .txt file")
    print()
    choice = input(" Which option would you like to choose? ")
    if choice == "1":
        RandomizeAbilities()
    elif choice == "2":
        RandomizeStrength()
    elif choice == "3":
        RandomizeDestruction()
    elif choice == "4":
        RandomizeDurability()
    elif choice == "5":
        RandomizeMoveSpeed()
    elif choice == "6":
        RandomizeReactionSpeed()
    elif choice == "7":
        RandomizeIntelligence()
    elif choice == "8":
        RandomizeStamina()
    elif choice == "9":
        RandomizeRange()
    elif choice == "10":
        RandomizeWeakness()
    elif choice == "11":
        RandomizeAbilitiesAll()
        RandomizeStrengthAll()
        RandomizeDestructionAll()
        RandomizeDurabilityAll()
        RandomizeMoveSpeedAll()
        RandomizeReactionSpeedAll()
        RandomizeIntelligenceAll()
        RandomizeStaminaAll()
        RandomizeRangeAll()
        RandomizeWeaknessAll()
    elif choice == "12":
        DisplayFullStats()
    elif choice == "13":
        ClearSavedCharacter()
    elif choice == "14":
        SaveCharacter()
    else:
        print(" Incorrect choice, try again!")
        time.sleep(1)
        MainMenu()

def NameCharacter():
    global CharacterName
    CharacterName = input(" Name your character: ")
    MainMenu()

def RandomizeAbilities():
    global GeneratedAbilitiesList
    GeneratedAbilitiesList = []
    NumberOfAbilities = int(input(" How many abilities do you want your character to have? (1-100, leave 0 for random (random is capped at 15 abilities)) "))
    if NumberOfAbilities == 0:
        NumberOfAbilities = random.randint(1,15)
    elif NumberOfAbilities < 0:
        print(" You must have at least one ability")
        time.sleep(1)
        MainMenu()
    elif NumberOfAbilities > 100:
        print(" You can at most have 100 abilities")
        time.sleep(1)
        MainMenu()
    GeneratedAbilities = 0
    AbilitiesDictionary = open("Abilities.txt", "r")
    Abilities = AbilitiesDictionary.read()
    ListOfTiers = Abilities.split(",")
    while GeneratedAbilities < NumberOfAbilities:
        RandomizedAbility = random.choice(ListOfTiers)
        ListOfTiers.remove(RandomizedAbility)
        print(" Your character's Ability is:", RandomizedAbility)
        GeneratedAbilitiesList.append(RandomizedAbility)
        GeneratedAbilities += 1
    time.sleep(2)
    MainMenu()

def RandomizeStrength():
    global RandomizedStrength
    StrengthTiersDictionary = open("Strength Tiers.txt", "r")
    StrengthTiers = StrengthTiersDictionary.read()
    ListOfTiers = StrengthTiers.split(",")
    RandomizedStrength = random.choice(ListOfTiers)
    print(" Your character's Physical Strength is:", RandomizedStrength)
    time.sleep(1)
    MainMenu()

def RandomizeDestruction():
    global RandomizedDestruction
    DestructionTiersDictionary = open("Strength Tiers.txt", "r")
    DestructionTiers = DestructionTiersDictionary.read()
    ListOfTiers = DestructionTiers.split(",")
    RandomizedDestruction = random.choice(ListOfTiers)
    print(" Your character's Attack Potency/Destructive Capacity is:", RandomizedDestruction)
    time.sleep(1)
    MainMenu()

def RandomizeDurability():
    global RandomizedDurability
    DurabilityTiersDictionary = open("Strength Tiers.txt", "r")
    DurabilityTiers = DurabilityTiersDictionary.read()
    ListOfTiers = DurabilityTiers.split(",")
    RandomizedDurability = random.choice(ListOfTiers)
    print(" Your character's Durability is:", RandomizedDurability)
    time.sleep(1)
    MainMenu()

def RandomizeMoveSpeed():
    global RandomizedMoveSpeed
    MoveSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    MoveSpeedTiers = MoveSpeedTiersDictionary.read()
    ListOfTiers = MoveSpeedTiers.split(",")
    RandomizedMoveSpeed = random.choice(ListOfTiers)
    print(" Your character's Movement Speed is:", RandomizedMoveSpeed)
    time.sleep(1)
    MainMenu()

def RandomizeReactionSpeed():
    global RandomizedReactSpeed
    ReactSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    ReactSpeedTiers = ReactSpeedTiersDictionary.read()
    ListOfTiers = ReactSpeedTiers.split(",")
    RandomizedReactSpeed = random.choice(ListOfTiers)
    print(" Your character's Reaction Speed is:", RandomizedReactSpeed)
    time.sleep(1)
    MainMenu()

def RandomizeIntelligence():
    global RandomizedIntelligence
    IntelligenceTiersDictionary = open("Intelligence Tiers.txt", "r")
    IntelligenceTiers = IntelligenceTiersDictionary.read()
    ListOfTiers = IntelligenceTiers.split(",")
    RandomizedIntelligence = random.choice(ListOfTiers)
    print(" Your character's Intelligence is:", RandomizedIntelligence)
    time.sleep(1)
    MainMenu()

def RandomizeStamina():
    global RandomizedStamina
    StaminaTiersDictionary = open("Stamina Tiers.txt", "r")
    StaminaTiers = StaminaTiersDictionary.read()
    ListOfTiers = StaminaTiers.split(",")
    RandomizedStamina = random.choice(ListOfTiers)
    print(" Your character's Stamina is:", RandomizedStamina)
    time.sleep(1)
    MainMenu()

def RandomizeRange():
    global RandomizedRange
    RangeTiersDictionary = open("Range Tiers.txt", "r")
    RangeTiers = RangeTiersDictionary.read()
    ListOfTiers = RangeTiers.split(",")
    RandomizedRange = random.choice(ListOfTiers)
    print(" Your character's Range is:", RandomizedRange)
    time.sleep(1)
    MainMenu()

def RandomizeWeakness():
    global GeneratedWeaknessesList
    GeneratedWeaknessesList = []
    NumberOfWeaknesses = random.randint(0,4)
    GeneratedWeaknesses = 0
    WeaknessDictionary = open("Weaknesses.txt", "r")
    Weakness = WeaknessDictionary.read()
    ListOfTiers = Weakness.split(",")
    if NumberOfWeaknesses == 0:
        print(" You have no Weaknesses!")
    else:
        while GeneratedWeaknesses < NumberOfWeaknesses:
            RandomizedWeaknesses = random.choice(ListOfTiers)
            ListOfTiers.remove(RandomizedWeaknesses)
            print(" Your character's Weakness is:", RandomizedWeaknesses)
            GeneratedWeaknessesList.append(RandomizedWeaknesses)
            GeneratedWeaknesses += 1
    time.sleep(1)
    MainMenu()

def RandomizeAbilitiesAll():
    global GeneratedAbilitiesList
    GeneratedAbilitiesList = []
    NumberOfAbilities = int(input(" How many abilities do you want your character to have? (1-100, leave 0 for random) "))
    if NumberOfAbilities == 0:
        NumberOfAbilities = random.randint(1,15)
    elif NumberOfAbilities < 0:
        print(" You must have at least one ability")
        time.sleep(1)
        MainMenu()
    elif NumberOfAbilities > 100:
        print(" You can at most have 100 abilities")
        time.sleep(1)
        MainMenu()
    GeneratedAbilities = 0
    AbilitiesDictionary = open("Abilities.txt", "r")
    Abilities = AbilitiesDictionary.read()
    ListOfTiers = Abilities.split(",")
    while GeneratedAbilities < NumberOfAbilities:
        RandomizedAbility = random.choice(ListOfTiers)
        ListOfTiers.remove(RandomizedAbility)
        print(" Your character's Ability is:", RandomizedAbility)
        GeneratedAbilitiesList.append(RandomizedAbility)
        GeneratedAbilities += 1
    time.sleep(2)

def RandomizeStrengthAll():
    global RandomizedStrength
    StrengthTiersDictionary = open("Strength Tiers.txt", "r")
    StrengthTiers = StrengthTiersDictionary.read()
    ListOfTiers = StrengthTiers.split(",")
    RandomizedStrength = random.choice(ListOfTiers)
    print(" Your character's Physical Strength is:", RandomizedStrength)
    time.sleep(1)

def RandomizeDestructionAll():
    global RandomizedDestruction
    DestructionTiersDictionary = open("Strength Tiers.txt", "r")
    DestructionTiers = DestructionTiersDictionary.read()
    ListOfTiers = DestructionTiers.split(",")
    RandomizedDestruction = random.choice(ListOfTiers)
    print(" Your character's Attack Potency/Destructive Capacity is:", RandomizedDestruction)
    time.sleep(1)

def RandomizeDurabilityAll():
    global RandomizedDurability
    DurabilityTiersDictionary = open("Strength Tiers.txt", "r")
    DurabilityTiers = DurabilityTiersDictionary.read()
    ListOfTiers = DurabilityTiers.split(",")
    RandomizedDurability = random.choice(ListOfTiers)
    print(" Your character's Durability is:", RandomizedDurability)
    time.sleep(1)

def RandomizeMoveSpeedAll():
    global RandomizedMoveSpeed
    MoveSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    MoveSpeedTiers = MoveSpeedTiersDictionary.read()
    ListOfTiers = MoveSpeedTiers.split(",")
    RandomizedMoveSpeed = random.choice(ListOfTiers)
    print(" Your character's Movement Speed is:", RandomizedMoveSpeed)
    time.sleep(1)

def RandomizeReactionSpeedAll():
    global RandomizedReactSpeed
    ReactSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    ReactSpeedTiers = ReactSpeedTiersDictionary.read()
    ListOfTiers = ReactSpeedTiers.split(",")
    RandomizedReactSpeed = random.choice(ListOfTiers)
    print(" Your character's Reaction Speed is:", RandomizedReactSpeed)
    time.sleep(1)

def RandomizeIntelligenceAll():
    global RandomizedIntelligence
    IntelligenceTiersDictionary = open("Intelligence Tiers.txt", "r")
    IntelligenceTiers = IntelligenceTiersDictionary.read()
    ListOfTiers = IntelligenceTiers.split(",")
    RandomizedIntelligence = random.choice(ListOfTiers)
    print(" Your character's Intelligence is:", RandomizedIntelligence)
    time.sleep(1)

def RandomizeStaminaAll():
    global RandomizedStamina
    StaminaTiersDictionary = open("Stamina Tiers.txt", "r")
    StaminaTiers = StaminaTiersDictionary.read()
    ListOfTiers = StaminaTiers.split(",")
    RandomizedStamina = random.choice(ListOfTiers)
    print(" Your character's Stamina is:", RandomizedStamina)
    time.sleep(1)

def RandomizeRangeAll():
    global RandomizedRange
    RangeTiersDictionary = open("Range Tiers.txt", "r")
    RangeTiers = RangeTiersDictionary.read()
    ListOfTiers = RangeTiers.split(",")
    RandomizedRange = random.choice(ListOfTiers)
    print(" Your character's Range is:", RandomizedRange)
    time.sleep(1)

def RandomizeWeaknessAll():
    global GeneratedWeaknessesList
    GeneratedWeaknessesList = []
    NumberOfWeaknesses = random.randint(0,4)
    GeneratedWeaknesses = 0
    WeaknessDictionary = open("Weaknesses.txt", "r")
    Weakness = WeaknessDictionary.read()
    ListOfTiers = Weakness.split(",")
    if NumberOfWeaknesses == 0:
        print(" You have no Weaknesses!")
    else:
        while GeneratedWeaknesses < NumberOfWeaknesses:
            RandomizedWeaknesses = random.choice(ListOfTiers)
            ListOfTiers.remove(RandomizedWeaknesses)
            print(" Your character's Weakness is:", RandomizedWeaknesses)
            GeneratedWeaknessesList.append(RandomizedWeaknesses)
            GeneratedWeaknesses += 1
    time.sleep(1)
    MainMenu()


def DisplayFullStats():
    #AbilityList = ", ".join(GeneratedAbilitiesList)
    #WeaknessList = ", ".join(GeneratedWeaknessesList)
    print()
    print()
    print(" The stats of your character", CharacterName, "are as follows:")
    print()
    print(" Your characters Abilities are", GeneratedAbilitiesList)
    print(" Your characters Physical Strength is", RandomizedStrength)
    print(" Your characters Attack Potency/Destructive Capacity is", RandomizedDestruction)
    print(" Your characters Durability is", RandomizedDurability)
    print(" Your characters Movement Speed is", RandomizedMoveSpeed)
    print(" Your characters Reaction Speed is", RandomizedReactSpeed)
    print(" Your characters Intelligence is", RandomizedIntelligence)
    print(" Your characters Stamina is", RandomizedStamina)
    print(" Your characters Range is", RandomizedRange)
    print(" Your characters Weaknesses are", GeneratedWeaknessesList)
    print()
    print(" Press any key to continue...")
    m.getch()
    MainMenu()

def ClearSavedCharacter():
    global RandomizedStrength
    global RandomizedDestruction
    global RandomizedDurability
    global RandomizedMoveSpeed
    global RandomizedReactSpeed
    global RandomizedIntelligence
    global RandomizedStamina
    global RandomizedRange
    GeneratedAbilitiesList.clear()
    GeneratedWeaknessesList.clear()
    RandomizedStrength = None
    RandomizedDestruction = None
    RandomizedDurability = None
    RandomizedMoveSpeed = None
    RandomizedReactSpeed = None
    RandomizedIntelligence = None
    RandomizedStamina = None
    RandomizedRange = None
    print(" Your character has been cleared successfully")
    time.sleep(1)
    MainMenu()

def SaveCharacter():
    AbilityList = ", ".join(GeneratedAbilitiesList)
    WeaknessList = ", ".join(GeneratedWeaknessesList)
    with open(CharacterName + ".txt", "w") as fw:
        fw.write("Character Sheet - "+CharacterName+'\n')
    with open(CharacterName + ".txt", "a") as fa:
        fa.write('\n')
        fa.write("Abilities:"+'\n')
        fa.write(AbilityList+'\n')
        fa.write('\n')
        fa.write("- Stats -"+'\n')
        fa.write("Physical Strength: "+RandomizedStrength+'\n')
        fa.write("Attack Potency/Destructive Capacity: "+RandomizedDestruction+'\n')
        fa.write("Durability: "+RandomizedDurability+'\n')
        fa.write("Movement Speed: "+RandomizedMoveSpeed+'\n')
        fa.write("Reaction Speed: "+RandomizedReactSpeed+'\n')
        fa.write("Intelligence: "+RandomizedIntelligence+'\n')
        fa.write("Stamina: "+RandomizedStamina+'\n')
        fa.write("Range: "+RandomizedRange+'\n')
        fa.write("Weaknesses:"+'\n')
        fa.write(WeaknessList)
    print()
    print(" Your character was saved to", CharacterName+".txt")
    print(" Press any key to continue...")
    m.getch()
    MainMenu()

NameCharacter()