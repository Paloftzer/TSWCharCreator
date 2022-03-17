import random
import time
import msvcrt as m
import os
import os.path
import pygame # Currently unused, going to hopefully make a true ui for it with pygame 

if os.path.exists("Characters"):
    pass
else:
    os.makedirs("Characters")

save_path = "./Characters/"

GeneratedWeaknesses = 0

GeneratedAbilitiesList = []
GeneratedWeaknessesList = []
RandomizedStrength = None
RandomizedDestruction = None
RandomizedDurability = None
RandomizedMoveSpeed = None
RandomizedReactSpeed = None
RandomizedIntelligence = None
RandomizedStamina = None
RandomizedRange = None

AbilitiesList = ["Absolute Zero,Power Absorption,Energy Absorption,Life-Force Absorption,Biological Absorption,Abstract Existence (Type 1),Abstract Existence (Type 2),Time Paradox Immunity (Acausality),Temporal Singularity (Acausality),Temporal Permanence (Acausality),Irregular Causality (Acausality),Causality Transcendence (Acausality),Acid Manipulation,Acupuncture,Biological Adaptation,Physiological Adaptation,Psychological Adaptation,Technical Adaptation,Informational Adaptation,Afterimages,Age Manipulation,Manipulation of Animals,Manipulation of Mythical Creatures,Astral Projection,Attack Reflection,Explosive Aura,Overwhelming Aura,Fear-inducing Aura,Rage-inducing Aura,Materialized Aura,Catastrophe-inducing Aura,Charismatic Aura,Avatar Creation,Berserk Mode,Battle Field Removal,Biological Manipulation,Blood Manipulation as the Liquid,Blood Manipulation as a Source of Energy,Blood Manipulation as an Information Object,Blood Magic,Body Control (Basic Functions),Body Control (Advanced Control),Body Control (Control of the Body),Body Control (Control of Cells),Body Control (Control of Microparticles),Causality Manipulation,Clairvoyance,Conceptual Manipulation,Corruption (Type 1),Corruption (Type 2),Corruption (Type 3),Creation,Crystal Manipulation,Curse Manipulation,Damage Boost,Damage Reduction,Danmaku,Darkness Manipulation,Death Manipulation,Devil Physiology,Dream Eaters Physiology,Dream Manipulation,Split Duplication,One to One Duplication,Durability Negation,Earthbending,Earth Element Control,Earth Release,Geokinesis,Terrakinesis,Electric/Current manipulation,Electrokinesis,Fulgurkinesis,Electric Charge Manipulation,Lightning Bending,Lightning Element Control,Lightning Release,Elemental Manipulation,Energy Manipulation,Energy Projection,Enhanced Awareness,Enhanced Hearing,Enhanced Vision,Enhanced Smell,Enhanced Taste,Enhanced Touch,Enhanced Sixth,Extra Senses,Existence Erasure,Explosion Manipulation,Fate Manipulation,Agnikinesis,Fire Element Control,Fire Release,Firebending,Flame Control,Ignikinesis,Pyrokinesis,Pseudo Flight,True Flight,Levitation,Forcefield,Fourth Wall Awareness,Fusionism,Negative Gravity Manipulation,Positive Gravity Manipulation,Full Gravity Manipulation,Healing (Weak),Healing (Normal),Healing (Strong),Healing (Fully),Heartless Physiology,Heat Manipulation,Hyper-Dimensional,Beyond-Dimensional,Higher Dimensional Manipulation,Holy Manipulation,Homing Attack,Ice Manipulation,Illusion Creation,Eternal Life,Immortality without Regeneration,Immortality via Regeneration,Immortality via Self-Resurrection,Immortality via Replacements,Parasitic,Undead,Reliant Immortality,Transcendental Immortality,Meta-Immortality,Deathless Immortality,Pseudo Intangibility,Spatial Intangibility,Phasing,Intangibility,Invisibility,Invulnerability,Law Manipulation,Life Manipulation,Light Manipulation,Longevity,Magic,Magma Manipulation,Magnetism Manipulation,Martial Arts,Matter Manipulation,Metal Manipulation,Mind Manipulation,Necromancy,Noble Physiology,Nobody Physiology,Non-Corporeal,Non-Physical Interaction,Omnipotence,Pain Manipulation,Perception Manipulation,Petrification,Plant Manipulation,Plot Manipulation,Pocket Reality Manipulation,Poison Manipulation,Possession,Power Bestowal,Power Mimicry,Power Nullification,Precognition,Presence Concealment,Probability Manipulation,Quantum Manipulation,Radiation Manipulation,Reactive Evolution,Reality Warping,Regeneration,Elemental Resistance,Energy Resistance,Mental Resistance,Resurrection,Retrocognition,Sand Manipulation,Sealing,Self-Sustenance,Shapeshifting,Size Manipulation,Soul Manipulation,Sound Manipulation,Spatial Manipulation,Star Platinum,The World,King Crimson,Killer Queen,Gold Experience,Crazy Diamond,Statistics Amplification,Statistics Reduction,Superhuman Physical Characteristics,Technology Manipulation,Telekinesis,Telepathy,Teleportation,Thread Manipulation,Time Stop,Time Rewind,Time Skip,Speed up Time,Slow down Time,Toon Force,Undead Physiology,Underwater Breathing,Vector Manipulation,Void Manipulation,Aquakinesis,Hydrokinesis,Water Element Control,Water Release,Waterbending,Weapon Mastery,Weather Manipulation,Wind Manipulation"]
StrengthList = ["Flatland,Micro,Dwarf,Below Human,Human,Street,Superhuman,Superhuman+,Wall,Wall+,Small Building,Small Building+,Building,Building+,Large Building,Large Building+,City Block,City Block+,Multi Block,Multi Block+,Town,Town+,City,City+,Mountain,Mountain+,Island,Island+,Country,Country+,Large Country/Small Continent,Large Country+/Small Continent+,Continent,Continent+,Multi-Continent,Multi-Continent+,Moon,Moon+,Small Planet,Small Planet+,Planet,Planet+,Large Planet,Large Planet+,Small Star,Small Star+,Star,Star+,Large Star,Large Star+,Solar System,Solar System+,Multi-Solar System,Multi-Solar System+,Galaxy,Galaxy+,Multi-Galaxy,Multi-Galaxy+,Low Universe,Universe,High Universe,Universe+,Low Multiverse,Low Multiverse+,Multiverse,Multiverse+,High Multiverse,High Multiverse+,Hyper Dimensional,Hyper Dimensional+,High Hyper Dimensional,High Hyper Dimensional+,Transcendent,Transcendent+,Absolute Infinity"]
SpeedList = ["Stationary,Sub-Human,Human,High Human,Peak Human,Superhuman,Faster Than The Eye Can See/FTE,Transonic,Supersonic,Supersonic+,Hypersonic,High Hypersonic,High Hypersonic+,Massively Hypersonic,Massively Hypersonic+,Sub-Relativistic,Sub-Relativistic+,Relativistic,Relativistic+,Lightspeed/SOL,FTL,FTL+,FTLx,MFTL,MFTL+,MFTLx,TransUniversal,TransUniversal+,TransUniversalx,TFTC,TFTC+,TFTCx,Infinite,Immeasurable,Irrelevant,Omnipresent,Nigh-Omnipresence"]
IntelligenceList = ["None,Animal-like,Very low,Low,Below average,Average,Above average,High,Very high,Genius,Super genius,Hyper genius,Cosmic genius,Nigh omniscient,Omniscient"]
StaminaList = ["None,Very low,Low,Below average,Average,Above average,High,Very High,Extremely high,Nigh limitless,Limitless"]
RangeList = ["Melee,Extended Melee,Several meters,Tens of meters,Hundreds of meters,Kilometers,Tens of Kilometers,Hundreds of Kilometers,Thousands of Kilometers,Planetary Range,Stellar,Solar system,Multi solar system,Galactic,Multi galactic,Universal,High-Universal,Universal+,Low Multiversal,Multiversal,High Multiversal,Hyper Dimensional,High Hyper Dimensional,Transcendent,Absolute Infinity"]
WeaknessesList = ["Slow Start,Heavy Strain,Low Temper,Ability Backlash,Arrogant Nature,Asthma,Easily distracted,Flat Earther,Grounded,Fear of Heights,Social Anxiety,Lazy,Unstable abilities,Gambling addict"]
ItemList = ["Senzu Bean,Power Pole,Z Sword,Infinity Gauntlet,Death Note,Excalibur,Durandal,Mons Meg,Trident,Mjolnir,Gungnir,Armor of Achilles,Pridwen,Aegis,Infinite Quiver,Gun,Talaria,Arrow of Brahma,Asi,Sharanga,Gram,Gae Bulg,Muramasa,Kusanagi,Colada,Panacea,The Holy Grail,Kavacha,Helmet of Rostam,Tarnhelm,Cap of Invisibility,Green Armor,Crown of Immortality,Cloud-stepping Boots"]

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
    if not GeneratedAbilitiesList:
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
        try:
            AbilitiesDictionary = open("Abilities.txt", "r")
        except:
            textfile = open("Abilities.txt", "w")
            for element in AbilitiesList:
                textfile.write(element)
            textfile.close()
        finally:
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
    else:
        print(" You have already generated abilities!")
        time.sleep(1)
        MainMenu()

def RandomizeStrength():
    global RandomizedStrength
    if RandomizedStrength != None:
        print(" You already have a strength tier!")
        time.sleep(1)
        MainMenu()
    try:
        StrengthTiersDictionary = open("Strength Tiers.txt", "r")
    except:
        textfile = open("Strength Tiers.txt", "w")
        for element in StrengthList:
            textfile.write(element)
        textfile.close()
    finally:
        StrengthTiersDictionary = open("Strength Tiers.txt", "r")
    StrengthTiers = StrengthTiersDictionary.read()
    ListOfTiers = StrengthTiers.split(",")
    RandomizedStrength = random.choice(ListOfTiers)
    print(" Your character's Physical Strength is:", RandomizedStrength)
    time.sleep(1)
    MainMenu()

def RandomizeDestruction():
    global RandomizedDestruction
    if RandomizedDestruction != None:
        print(" You already have a destruction tier!")
        time.sleep(1)
        MainMenu()
    try:
        DestructionTiersDictionary = open("Strength Tiers.txt", "r")
    except:
        textfile = open("Strength Tiers.txt", "w")
        for element in StrengthList:
            textfile.write(element)
        textfile.close()
    finally:
        DestructionTiersDictionary = open("Strength Tiers.txt", "r")
    DestructionTiers = DestructionTiersDictionary.read()
    ListOfTiers = DestructionTiers.split(",")
    RandomizedDestruction = random.choice(ListOfTiers)
    print(" Your character's Attack Potency/Destructive Capacity is:", RandomizedDestruction)
    time.sleep(1)
    MainMenu()

def RandomizeDurability():
    global RandomizedDurability
    if RandomizedDurability != None:
        print(" You already have a durability tier!")
        time.sleep(1)
        MainMenu()
    try:
        DurabilityTiersDictionary = open("Strength Tiers.txt", "r")
    except:
        textfile = open("Strength Tiers.txt", "w")
        for element in StrengthList:
            textfile.write(element)
        textfile.close()
    finally:
        DurabilityTiersDictionary = open("Strength Tiers.txt", "r")
    DurabilityTiers = DurabilityTiersDictionary.read()
    ListOfTiers = DurabilityTiers.split(",")
    RandomizedDurability = random.choice(ListOfTiers)
    print(" Your character's Durability is:", RandomizedDurability)
    time.sleep(1)
    MainMenu()

def RandomizeMoveSpeed():
    global RandomizedMoveSpeed
    if RandomizedMoveSpeed != None:
        print(" You already have a movement speed tier!")
        time.sleep(1)
        MainMenu()
    try:
        MoveSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    except:
        textfile = open("Speed Tiers.txt", "w")
        for element in SpeedList:
            textfile.write(element)
        textfile.close()
    finally:
        MoveSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    MoveSpeedTiers = MoveSpeedTiersDictionary.read()
    ListOfTiers = MoveSpeedTiers.split(",")
    RandomizedMoveSpeed = random.choice(ListOfTiers)
    print(" Your character's Movement Speed is:", RandomizedMoveSpeed)
    time.sleep(1)
    MainMenu()

def RandomizeReactionSpeed():
    global RandomizedReactSpeed
    if RandomizedReactSpeed != None:
        print(" You already have a reaction speed tier!")
        time.sleep(1)
        MainMenu()
    try:
        ReactSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    except:
        textfile = open("Speed Tiers.txt", "w")
        for element in SpeedList:
            textfile.write(element)
        textfile.close()
    finally:
        ReactSpeedTiersDictionary = open("Speed Tiers.txt", "r")
    ReactSpeedTiers = ReactSpeedTiersDictionary.read()
    ListOfTiers = ReactSpeedTiers.split(",")
    RandomizedReactSpeed = random.choice(ListOfTiers)
    print(" Your character's Reaction Speed is:", RandomizedReactSpeed)
    time.sleep(1)
    MainMenu()

def RandomizeIntelligence():
    global RandomizedIntelligence
    if RandomizedIntelligence != None:
        print(" You already have a intelligence tier!")
        time.sleep(1)
        MainMenu()
    try:
        IntelligenceTiersDictionary = open("Intelligence Tiers.txt", "r")
    except:
        textfile = open("Intelligence Tiers.txt", "w")
        for element in IntelligenceList:
            textfile.write(element)
        textfile.close()
    finally:
        IntelligenceTiersDictionary = open("Intelligence Tiers.txt", "r")
    IntelligenceTiers = IntelligenceTiersDictionary.read()
    ListOfTiers = IntelligenceTiers.split(",")
    RandomizedIntelligence = random.choice(ListOfTiers)
    print(" Your character's Intelligence is:", RandomizedIntelligence)
    time.sleep(1)
    MainMenu()

def RandomizeStamina():
    global RandomizedStamina
    if RandomizedStamina != None:
        print(" You already have a stamina tier!")
        time.sleep(1)
        MainMenu()
    try:
        StaminaTiersDictionary = open("Stamina Tiers.txt", "r")
    except:
        textfile = open("Stamina Tiers.txt", "w")
        for element in StaminaList:
            textfile.write(element)
        textfile.close()
    finally:
        StaminaTiersDictionary = open("Stamina Tiers.txt", "r")
    StaminaTiers = StaminaTiersDictionary.read()
    ListOfTiers = StaminaTiers.split(",")
    RandomizedStamina = random.choice(ListOfTiers)
    print(" Your character's Stamina is:", RandomizedStamina)
    time.sleep(1)
    MainMenu()

def RandomizeRange():
    global RandomizedRange
    if RandomizedRange != None:
        print(" You already have a range tier!")
        time.sleep(1)
        MainMenu()
    try:
        RangeTiersDictionary = open("Range Tiers.txt", "r")
    except:
        textfile = open("Range Tiers.txt", "w")
        for element in RangeList:
            textfile.write(element)
        textfile.close()
    finally:
        RangeTiersDictionary = open("Range Tiers.txt", "r")
    RangeTiers = RangeTiersDictionary.read()
    ListOfTiers = RangeTiers.split(",")
    RandomizedRange = random.choice(ListOfTiers)
    print(" Your character's Range is:", RandomizedRange)
    time.sleep(1)
    MainMenu()

def RandomizeWeakness():
    global GeneratedWeaknesses
    if GeneratedWeaknesses == 0:
        if not GeneratedWeaknessesList:
            NumberOfWeaknesses = random.randint(0,4)
            try:
                WeaknessDictionary = open("Weaknesses.txt", "r")
            except:
                textfile = open("Weaknesses.txt", "w")
                for element in WeaknessesList:
                    textfile.write(element)
                textfile.close()
            finally:
                WeaknessDictionary = open("Weaknesses.txt", "r")
            Weakness = WeaknessDictionary.read()
            ListOfTiers = Weakness.split(",")
            if NumberOfWeaknesses == 0:
                print(" You have no Weaknesses!")
                GeneratedWeaknesses += 1
            else:
                while GeneratedWeaknesses < NumberOfWeaknesses:
                    RandomizedWeaknesses = random.choice(ListOfTiers)
                    ListOfTiers.remove(RandomizedWeaknesses)
                    print(" Your character's Weakness is:", RandomizedWeaknesses)
                    GeneratedWeaknessesList.append(RandomizedWeaknesses)
                    GeneratedWeaknesses += 1
            time.sleep(1)
            MainMenu()
        else:
            print(" You have already generated weaknesses!")
            time.sleep(1)
            MainMenu()
    else:
        print(" You have already generated weaknesses!")
        time.sleep(1)
        MainMenu()

def RandomizeAbilitiesAll():
    if not GeneratedAbilitiesList:
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
        try:
            AbilitiesDictionary = open("Abilities.txt", "r")
        except:
            textfile = open("Abilities.txt", "w")
            for element in AbilitiesList:
                textfile.write(element)
            textfile.close()
        finally:
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
    else:
        print(" You have already generated abilities!")
        time.sleep(1)

def RandomizeStrengthAll():
    global RandomizedStrength
    if RandomizedStrength != None:
        print(" You already have a strength tier!")
        time.sleep(1)
    else:
        try:
            StrengthTiersDictionary = open("Strength Tiers.txt", "r")
        except:
            textfile = open("Strength Tiers.txt", "w")
            for element in StrengthList:
                textfile.write(element)
            textfile.close()
        finally:
            StrengthTiersDictionary = open("Strength Tiers.txt", "r")
        StrengthTiers = StrengthTiersDictionary.read()
        ListOfTiers = StrengthTiers.split(",")
        RandomizedStrength = random.choice(ListOfTiers)
        print(" Your character's Physical Strength is:", RandomizedStrength)
        time.sleep(1)

def RandomizeDestructionAll():
    global RandomizedDestruction
    if RandomizedDestruction != None:
        print(" You already have a destruction tier!")
        time.sleep(1)
    else:
        try:
            DestructionTiersDictionary = open("Strength Tiers.txt", "r")
        except:
            textfile = open("Strength Tiers.txt", "w")
            for element in StrengthList:
                textfile.write(element)
            textfile.close()
        finally:
            DestructionTiersDictionary = open("Strength Tiers.txt", "r")
        DestructionTiers = DestructionTiersDictionary.read()
        ListOfTiers = DestructionTiers.split(",")
        RandomizedDestruction = random.choice(ListOfTiers)
        print(" Your character's Attack Potency/Destructive Capacity is:", RandomizedDestruction)
        time.sleep(1)

def RandomizeDurabilityAll():
    global RandomizedDurability
    if RandomizedDurability != None:
        print(" You already have a durability tier!")
        time.sleep(1)
    else:
        try:
            DurabilityTiersDictionary = open("Strength Tiers.txt", "r")
        except:
            textfile = open("Strength Tiers.txt", "w")
            for element in StrengthList:
                textfile.write(element)
            textfile.close()
        finally:
            DurabilityTiersDictionary = open("Strength Tiers.txt", "r")
        DurabilityTiers = DurabilityTiersDictionary.read()
        ListOfTiers = DurabilityTiers.split(",")
        RandomizedDurability = random.choice(ListOfTiers)
        print(" Your character's Durability is:", RandomizedDurability)
        time.sleep(1)

def RandomizeMoveSpeedAll():
    global RandomizedMoveSpeed
    if RandomizedMoveSpeed != None:
        print(" You already have a movement speed tier!")
        time.sleep(1)
    else:
        try:
            MoveSpeedTiersDictionary = open("Speed Tiers.txt", "r")
        except:
            textfile = open("Speed Tiers.txt", "w")
            for element in SpeedList:
                textfile.write(element)
            textfile.close()
        finally:
            MoveSpeedTiersDictionary = open("Speed Tiers.txt", "r")
        MoveSpeedTiers = MoveSpeedTiersDictionary.read()
        ListOfTiers = MoveSpeedTiers.split(",")
        RandomizedMoveSpeed = random.choice(ListOfTiers)
        print(" Your character's Movement Speed is:", RandomizedMoveSpeed)
        time.sleep(1)

def RandomizeReactionSpeedAll():
    global RandomizedReactSpeed
    if RandomizedReactSpeed != None:
        print(" You already have a reaction speed tier!")
        time.sleep(1)
    else:
        try:
            ReactSpeedTiersDictionary = open("Speed Tiers.txt", "r")
        except:
            textfile = open("Speed Tiers.txt", "w")
            for element in SpeedList:
                textfile.write(element)
            textfile.close()
        finally:
            ReactSpeedTiersDictionary = open("Speed Tiers.txt", "r")
        ReactSpeedTiers = ReactSpeedTiersDictionary.read()
        ListOfTiers = ReactSpeedTiers.split(",")
        RandomizedReactSpeed = random.choice(ListOfTiers)
        print(" Your character's Reaction Speed is:", RandomizedReactSpeed)
        time.sleep(1)

def RandomizeIntelligenceAll():
    global RandomizedIntelligence
    if RandomizedIntelligence != None:
        print(" You already have a intelligence tier!")
        time.sleep(1)
    else:
        try:
            IntelligenceTiersDictionary = open("Intelligence Tiers.txt", "r")
        except:
            textfile = open("Intelligence Tiers.txt", "w")
            for element in IntelligenceList:
                textfile.write(element)
            textfile.close()
        finally:
            IntelligenceTiersDictionary = open("Intelligence Tiers.txt", "r")
        IntelligenceTiers = IntelligenceTiersDictionary.read()
        ListOfTiers = IntelligenceTiers.split(",")
        RandomizedIntelligence = random.choice(ListOfTiers)
        print(" Your character's Intelligence is:", RandomizedIntelligence)
        time.sleep(1)

def RandomizeStaminaAll():
    global RandomizedStamina
    if RandomizedStamina != None:
        print(" You already have a stamina tier!")
        time.sleep(1)
    else:
        try:
            StaminaTiersDictionary = open("Stamina Tiers.txt", "r")
        except:
            textfile = open("Stamina Tiers.txt", "w")
            for element in StaminaList:
                textfile.write(element)
            textfile.close()
        finally:
            StaminaTiersDictionary = open("Stamina Tiers.txt", "r")
        StaminaTiers = StaminaTiersDictionary.read()
        ListOfTiers = StaminaTiers.split(",")
        RandomizedStamina = random.choice(ListOfTiers)
        print(" Your character's Stamina is:", RandomizedStamina)
        time.sleep(1)

def RandomizeRangeAll():
    global RandomizedRange
    if RandomizedRange != None:
        print(" You already have a range tier!")
        time.sleep(1)
    else:
        try:
            RangeTiersDictionary = open("Range Tiers.txt", "r")
        except:
            textfile = open("Range Tiers.txt", "w")
            for element in RangeList:
                textfile.write(element)
            textfile.close()
        finally:
            RangeTiersDictionary = open("Range Tiers.txt", "r")
        RangeTiers = RangeTiersDictionary.read()
        ListOfTiers = RangeTiers.split(",")
        RandomizedRange = random.choice(ListOfTiers)
        print(" Your character's Range is:", RandomizedRange)
        time.sleep(1)

def RandomizeWeaknessAll():
    GeneratedWeaknesses = 0
    if not GeneratedWeaknessesList:
        NumberOfWeaknesses = random.randint(0,4)
        try:
            WeaknessDictionary = open("Weaknesses.txt", "r")
        except:
            textfile = open("Weaknesses.txt", "w")
            for element in WeaknessesList:
                textfile.write(element)
            textfile.close()
        finally:
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
    else:
        print(" You have already generated weaknesses!")
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
    global GeneratedWeaknesses
    GeneratedWeaknesses = 0
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
    NameCharacter()

def SaveCharacter():
    CompletePath = os.path.join(save_path, CharacterName+".txt")
    AbilityList = ", ".join(GeneratedAbilitiesList)
    WeaknessList = ", ".join(GeneratedWeaknessesList)
    with open(CompletePath, "w") as fw:
        fw.write("Character Sheet - "+CharacterName+'\n')
    with open(CompletePath, "a") as fa:
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
        fa.close()
    print()
    print(" Your character was saved to", CompletePath)
    print(" Press any key to continue...")
    m.getch()
    MainMenu()

NameCharacter()