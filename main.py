import random
import time

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
    else:
        print(" Incorrect choice, try again!")
        time.sleep(1)
        MainMenu()

def RandomizeAbilities():
    NumberOfAbilities = int(input(" How many abilities do you want your character to have? (1-100, leave 0 for random) "))
    if NumberOfAbilities == 0:
        NumberOfAbilities = random.randint(0,101)
    GeneratedAbilities = 0
    AbilitiesDictionary = open("Abilities.txt", "r")
    Abilities = AbilitiesDictionary.read()
    ListOfTiers = Abilities.split(",")
    while GeneratedAbilities < NumberOfAbilities:
        RandomizedAbility = random.choice(ListOfTiers)
        ListOfTiers.remove(RandomizedAbility)
        print(" Your character's Ability is: ", RandomizedAbility)
        GeneratedAbilities += 1
    time.sleep(3)
    MainMenu()

def RandomizeStrength():
    StrengthTiersDictionary = open("Strength Tiers.txt", "r")
    StrengthTiers = StrengthTiersDictionary.read()
    ListOfTiers = StrengthTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Physical Strength is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeDestruction():
    DestructionTiersDictionary = open("Strength Tiers.txt", "r")
    DestructionTiers = DestructionTiersDictionary.read()
    ListOfTiers = DestructionTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Attack Potency/Destructive Capacity is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeDurability():
    DurabilityTiersDictionary = open("Strength Tiers.txt", "r")
    DurabilityTiers = DurabilityTiersDictionary.read()
    ListOfTiers = DurabilityTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Durability is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeMoveSpeed():
    MoveSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    MoveSpeedTiers = MoveSpeedTiersDictionary.read()
    ListOfTiers = MoveSpeedTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Movement Speed is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeReactionSpeed():
    ReactSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    ReactSpeedTiers = ReactSpeedTiersDictionary.read()
    ListOfTiers = ReactSpeedTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Reaction Speed is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeIntelligence():
    IntelligenceTiersDictionary = open("Intelligence Tiers.txt", "r")
    IntelligenceTiers = IntelligenceTiersDictionary.read()
    ListOfTiers = IntelligenceTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Intelligence is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeStamina():
    StaminaTiersDictionary = open("Stamina Tiers.txt", "r")
    StaminaTiers = StaminaTiersDictionary.read()
    ListOfTiers = StaminaTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Stamina is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeRange():
    RangeTiersDictionary = open("Range Tiers.txt", "r")
    RangeTiers = RangeTiersDictionary.read()
    ListOfTiers = RangeTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Range is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeWeakness():
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
            print(" Your character's Weakness is: ", RandomizedWeaknesses)
            GeneratedWeaknesses += 1
    time.sleep(1)
    MainMenu()

def RandomizeAbilitiesAll():
    NumberOfAbilities = int(input(" How many abilities do you want your character to have? (1-100, leave 0 for random) "))
    if NumberOfAbilities == 0:
        NumberOfAbilities = random.randint(1,100)
    GeneratedAbilities = 0
    AbilitiesDictionary = open("Abilities.txt", "r")
    Abilities = AbilitiesDictionary.read()
    ListOfTiers = Abilities.split(",")
    while GeneratedAbilities < NumberOfAbilities:
        RandomizedAbility = random.choice(ListOfTiers)
        ListOfTiers.remove(RandomizedAbility)
        print(" Your character's Ability is: ", RandomizedAbility)
        GeneratedAbilities += 1
    time.sleep(3)

def RandomizeStrengthAll():
    StrengthTiersDictionary = open("Strength Tiers.txt", "r")
    StrengthTiers = StrengthTiersDictionary.read()
    ListOfTiers = StrengthTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Physical Strength is: ", RandomizedTier)
    time.sleep(1)

def RandomizeDestructionAll():
    DestructionTiersDictionary = open("Strength Tiers.txt", "r")
    DestructionTiers = DestructionTiersDictionary.read()
    ListOfTiers = DestructionTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Attack Potency/Destructive Capacity is: ", RandomizedTier)
    time.sleep(1)

def RandomizeDurabilityAll():
    DurabilityTiersDictionary = open("Strength Tiers.txt", "r")
    DurabilityTiers = DurabilityTiersDictionary.read()
    ListOfTiers = DurabilityTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Durability is: ", RandomizedTier)
    time.sleep(1)

def RandomizeMoveSpeedAll():
    MoveSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    MoveSpeedTiers = MoveSpeedTiersDictionary.read()
    ListOfTiers = MoveSpeedTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Movement Speed is: ", RandomizedTier)
    time.sleep(1)

def RandomizeReactionSpeedAll():
    ReactSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    ReactSpeedTiers = ReactSpeedTiersDictionary.read()
    ListOfTiers = ReactSpeedTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Reaction Speed is: ", RandomizedTier)
    time.sleep(1)

def RandomizeIntelligenceAll():
    IntelligenceTiersDictionary = open("Intelligence Tiers.txt", "r")
    IntelligenceTiers = IntelligenceTiersDictionary.read()
    ListOfTiers = IntelligenceTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Intelligence is: ", RandomizedTier)
    time.sleep(1)

def RandomizeStaminaAll():
    StaminaTiersDictionary = open("Stamina Tiers.txt", "r")
    StaminaTiers = StaminaTiersDictionary.read()
    ListOfTiers = StaminaTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Stamina is: ", RandomizedTier)
    time.sleep(1)

def RandomizeRangeAll():
    RangeTiersDictionary = open("Range Tiers.txt", "r")
    RangeTiers = RangeTiersDictionary.read()
    ListOfTiers = RangeTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print(" Your character's Range is: ", RandomizedTier)
    time.sleep(1)

def RandomizeWeaknessAll():
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
            print(" Your character's Weakness is: ", RandomizedWeaknesses)
            GeneratedWeaknesses += 1
    time.sleep(1)
    MainMenu()

MainMenu()