import random
import time

def MainMenu():
    print("-"*72)
    print("Hello and Welcome to the Top Strongest Wikia custom character generator!")
    print("-"*72)
    print()
    print()
    print("1 - Generate a custom or random amount of Abilities")
    print("2 - Generate a Characters Physical Strength")
    print("3 - Generate a Characters Attack Potency/Destructive Capacity")
    print("4 - Generate a Characters Durability")
    print("5 - Generate a Characters Movement Speed")
    print("6 - Generate a Characters Reaction Speed")
    print("7 - Generate a Characters Intelligence")
    choice = input("Which option would you like to choose? ")
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
    else:
        print("Incorrect choice, try again!")
        time.sleep(1)
        MainMenu()

def RandomizeAbilities():
    NumberOfAbilities = int(input("How many abilities do you want your character to have? (1-100, leave 0 for random) "))
    if NumberOfAbilities == 0:
        NumberOfAbilities = random.randint(0,101)
    GeneratedAbilities = 0
    while GeneratedAbilities < NumberOfAbilities:
        AbilitiesDictionary = open("Abilities.txt", "r")
        Abilities = AbilitiesDictionary.read()
        ListOfTiers = Abilities.split(",")
        RandomizedAbility = random.choice(ListOfTiers)
        print("Your character's Ability is: ", RandomizedAbility)
        GeneratedAbilities += 1
    time.sleep(5)
    MainMenu()

def RandomizeStrength():
    StrengthTiersDictionary = open("Strength Tiers.txt", "r")
    StrengthTiers = StrengthTiersDictionary.read()
    ListOfTiers = StrengthTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print("Your character's Physical Strength is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeDestruction():
    DestructionTiersDictionary = open("Strength Tiers.txt", "r")
    DestructionTiers = DestructionTiersDictionary.read()
    ListOfTiers = DestructionTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print("Your character's Attack Potency/Destructive Capacity is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeDurability():
    DurabilityTiersDictionary = open("Strength Tiers.txt", "r")
    DurabilityTiers = DurabilityTiersDictionary.read()
    ListOfTiers = DurabilityTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print("Your character's Durability is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeMoveSpeed():
    MoveSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    MoveSpeedTiers = MoveSpeedTiersDictionary.read()
    ListOfTiers = MoveSpeedTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print("Your character's Movement Speed is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeReactionSpeed():
    ReactSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    ReactSpeedTiers = ReactSpeedTiersDictionary.read()
    ListOfTiers = ReactSpeedTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print("Your character's Reaction Speed is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

def RandomizeIntelligence():
    IntelligenceTiersDictionary = open("Intelligence Tiers.txt", "r")
    IntelligenceTiers = IntelligenceTiersDictionary.read()
    ListOfTiers = IntelligenceTiers.split(",")
    RandomizedTier = random.choice(ListOfTiers)
    print("Your character's Intelligence is: ", RandomizedTier)
    time.sleep(1)
    MainMenu()

MainMenu()