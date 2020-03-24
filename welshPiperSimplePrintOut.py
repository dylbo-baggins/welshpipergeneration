import random

class Dice():
    results = []

    def addresult(self, num):
        self.results.append(num)

    def randomdieroll(self, sides, number):
        for x in range(number):
            self.addresult(random.randint(1,sides))

    def totalresults(self):
        return sum(self.results)

    def clearresults(self):
        self.results = []

    def rollresultsclear(self, sides, number):
        self.randomdieroll(sides, number)
        copyResults = self.results
        self.clearresults()
        return copyResults, sum(copyResults)

class AtlasHex():
    primaryterrain = ""
    surroundingsixhexes = []
    majorencounter = ""
    minorencounter = []

    def setprimaryterrain(self, terrain):
        self.primaryterrain = terrain

    def setsurroundingsixehexes(self, hexes):
        self.surroundingsixhexes = hexes

    def setmajorencounter(self, encounter):
        self.majorencounter = encounter

    def setminorencounter(self, encounter):
        self.minorencounter = encounter

    def getprimaryterrain(self):
        return self.primaryterrain
    def printhex(self):
        print("Primary Terrain: " + self.primaryterrain)
        print("Surround Terrain: " + str(self.surroundingsixhexes))
        print("Major encounter: " + self.majorencounter)
        print("Minor Encounters: " + str(self.minorencounter))




class Map():
    name = ""
    climate = ""
    climatemodifier= {"artic": -10, "sub-artic": -5, "temperate": 0, "sub-tropical": 5, "tropical": 10}
    majorminorchanceencounter = {"water": (10, 1), "swamp": (20, 2), "desert": (20, 2), "plains": (60, 6), "forest": (40, 4),
                      "hills": (40, 4), "mountains": (20, 2)}
    hexList = []
    waterprimedict = {"primary" : "water", "secondary" : "plains",
                      "tertiary": "forest", "wildcard": ["swamp", "desert", "hills"]}
    swampprimedict = {"primary": "swamp", "secondary": "plains", "tertiary": "forest",
                      "wildcard": ["water"]}
    desertprimedict = {"primary": "desert", "secondary": "hills",
                       "tertiary": "plains", "wildcard": ["water", "mountains"]}
    plainsprimedict = {"primary": "plains", "secondary": "forest",
                       "tertiary": "hills", "wildcard": ["water", "swamp", "desert"]}
    forestprimedict = {"primary": "forest", "secondary": "plains",
                       "tertiary": "hills", "wildcard": ["water", "swamp","mountains"]}
    hillsprimedict = {"primary": "hills", "secondary": "mountains",
                       "tertiary": "plains", "wildcard": ["water", "desert", "forest"]}
    mountainsprimedict = {"primary": "mountains", "secondary": "hills",
                       "tertiary": "forest", "wildcard": ["desert"]}
    primaryTerrainDictList = [waterprimedict, swampprimedict, desertprimedict, plainsprimedict, forestprimedict,
                              forestprimedict, hillsprimedict, mountainsprimedict, ]

    def generateSettlement(self):
        typeandpop = ""
        rulers = ""
        gov = ""
        alignment = ""
        commerce = ""
        quirk = ""
        diceSet = Dice()
        typeandpopList = ["Town, Pop: " + str(((diceSet.rollresultsclear(6, 3)[0][0])+2)*100),
                          "Town, Pop: " + str(((diceSet.rollresultsclear(6, 3)[0][0])+2)*100),
                          "Walled Town, Pop: " + str(((diceSet.rollresultsclear(6, 3)[0][0])+2)*100),
                          "City, Pop: " + str((diceSet.rollresultsclear(4, 3)[0][0])*1000),
                          "Walled City, Pop: " + str((diceSet.rollresultsclear(4, 3)[0][0])*1000),
                          "Walled Free City, Pop: " + str((diceSet.rollresultsclear(4, 3)[0][0])*1000),
                          "Walled Metropolis, Pop: " + str(((diceSet.rollresultsclear(6, 3)[0][0])+2)*3000),
                          "Walled City State, Pop: " + str(((diceSet.rollresultsclear(6, 3)[0][0])+2)*3000),]
        rulersList = ["Geriatrics", "Thieves", "Magi", "Military", "Merchants", "Scholars", "Secret Cult", "Adventurers", ]
        govList = ["Autocracy", "Bureaucracy", "Monarchy", "Oligarchy", "Syndicracy", "Theocracy", "Dictatorship", "Confederacy"]
        alignmentList = ["Lawful", "Lawful", "Neutral", "Neutral", "Neutral", "Chaotic", "Chaotic", "None", "None"]
        commerceList = ["Food", "Textiles", "Services", "Slaves", "Arms", "Minerals", "Livestock", "Booze"]
        rollresults = []

        # for x in range(5):
        #     rollresults.append(diceSet.rollresultsclear(8,1)[0][0])
        typeandpop = random.choice(typeandpopList)
        rulers = random.choice(rulersList)
        gender = diceSet.rollresultsclear(6,1)[0][0]
        if  gender <= 3:
            rulers = rulers + " (Men)"
        elif gender == 4:
            rulers = rulers + " (Women)"
        else:
            rulers = rulers + " (Men and Women)"
        gov = random.choice(govList)
        alignment = random.choice(alignmentList)
        commerce = random.choice(commerceList)

        evolList = ["some monster", "plant", "planar creature", "variant humanoid", "some sea creature", "off-world beings"]
        dwellslist = ["caves", "sonte fortifications", "buildings propped up on stilts", "trees", "organic structures", "restrictive abodes"]
        physicallylist = ["beautiful", "adpated for water", "odd height", "unusual hair/eye color", "potent", "inverted joint"]
        mentallylist = ["two steps ahead", "erudite", "empathetic", "unable to grasp specific concept", "naive", "ambidextrous"]
        expertslist = ["herb lore", "science", "engineering", "magic", "torture", "warfare"]
        rumoredtobelist = ["telepahtic", "asexual", "cannibalistic", "vampiric", "incestuous", "off-worlders"]
        architecturelist = ["skeletons", "insects", "plants & trees", "reptiles", "odd geometry", "water"]
        artisticallylist = ["sculpture", "painting", "literature", "performance", "pornography", "architecture"]
        fondnesslist = ["horses", "insects", "avians", "felines", "canines", "reptiles"]
        diplomacylist = ["force", "cold logic", "capitulation", "backroom deals", "intimidation", "betrayal"]
        stereotypelist = ["sea-farers", "thieves", "shrewd traders", "drunks", "backward", "lecherous"]
        socialperklist = ["polite", "tolerant", "hospitality", "merciful", "honest", "wise"]
        socialflawlist = ["proud", "quarrelsome", "vulgar", "vindictive", "austere", "garrulous"]
        adornmentlist = ["garish/sombre colors", "wispy garments", "masks", "shiny baubles", "body art", "exotic hides and furs"]
        stronglyinfluencedlist = ["colors", "astrology", "aloof whims", "reproductive need", "base urges", "weather patterns"]
        historicalfigurelist = ["saint", "matry", "traitor", "lowly beggar", "lunatic", "child"]
        affinityforlist = ["fire", "water", "air", "earth", "precious metals", "gemstones"]
        averstiontolist = ["magic", "water", "plants", "animals", "metal", "blood"]
        incapableoflist = ["deceit", "affection", "metaphor", "violence", "forgiveness", "sarcasm"]
        strangecustomlist = ["birth", "rite of passage", "marriage", "death", "rulership", "martial", "gender roles", "law & justice"]

        quirkList = ["Evolutionary trace of ", "Dwells within ", "Physically ", "Mentally ", "Considered experts in ",
                     "Widely rumoured to be ", "Architecture reminiscent of ", "Artistically prone toward ",
                     "Fondness for ", "Diplomacy characterised by ", "Stereotyped as ", "Social perk ", "Social flaw ",
                     "Adornment ", "Strongly influenced by ", "Historical figure was a ", "Affinity for ", "Aversion to ",
                     "Incapable of ", "Strange custom: "]
        listofquirklists = [ evolList, dwellslist, physicallylist, mentallylist, expertslist, rumoredtobelist, architecturelist, artisticallylist,
                            fondnesslist, diplomacylist, stereotypelist, socialperklist, socialflawlist, adornmentlist,
                             stronglyinfluencedlist, historicalfigurelist, affinityforlist, averstiontolist,
                             incapableoflist, strangecustomlist]
        birthlist = ["Children born at a certain moon phase are abandoned",
                     "Children are named after " + random.choice(["animal ", "relative "]) + "seen by the father following birth"
                     "Children born during an eclipse are afforded special status",
                     "Bastards are orphaned to a " + random.choice(["fighting order", "fighting order", "monastery", "monastery", "urchin's guild", "merchant navy"]),
                     "Children are taught to " + random.choice(["fight", "fight", "ride", "ride", "sneak", "swim"]) + " as soon as they can walk",
                     "Couples cannot have more than three " + random.choice(["offspring", "boys", "girls"])]
        riteofpassagelist = ["Receives vision of his blood enemy", "Must slay totem animal during sacred hunt",
                             "Must complete scavenger hunt in nearest city", "Must earn a “mannengild” to pay for adult status",
                             "Must choose a bride/get engaged", "Must attract a companion animal/familiar"]
        marriagelist = ["Divorce permitted, but belongings revert to husband’s chief rival",
                       "Husband may take multiple wives", "Consummation requires witness(es) and must occur within 24 hours",
                       "Ceremony must occur at an historical site", "Local lord may deflower the bride (i.e., so-called prima nocta)",
                       "Couple must abstain from some vice while engaged"]
        deathlist = ["Dead are (ritually) consumed by " + random.choice(["wild animals", "wild animals", "carrion birds", "decedent's totem animal", "carnivorous plant", "relatives"]),
                     "Dead are magically " + random.choice(["disintegrated", "disintegrated", "sent to astral plane", "shrunken", "petrified", "sunk into the earth"]),
                     "Dead are " + random.choice(["mummified", "thrown in a swamp", "interred at place of birth", "consigned to the waters", "cremated on a pyre", "left on a mountain peak"]),
                     "Dead ancestors are worshiped as family idols",
                     "Names of the dead may never be spoken",
                     "Body parts of the deceased are " + random.choice(["made into garments/jewellery", "made into garments/jewellery", "preserved in the home", "preserved in the home", "made into unguents", "strewn about the fields"])]
        rulershiplist = ["Ruler guided by parliament of " + random.choice(["the learned", "astrologers", "sorcerers", "savants", "supplicants", "past rulers' spirits"]),
                     "Rulers must be literate and demonstrate mastery of " + random.choice(["science", "math", "verse"]),
                     "Rulers required to pass " + random.choice(["mental test", "show of charity", "moral dilemma", "physical challenge", "logical paradox", "magical feat"]),
                     "Rulers ritually executed/assassinated upon removal of office",
                     "Contenders must best current ruler in " + random.choice(["single combat", "single combat", "ritual quest", "labyrinth", "wilderness survival", "withstanding poison"]),
                     "Ruler is rendered into a " + random.choice(["shapeshifter", "shapeshifter", "eunuch", "undead creature", "drug addict", "sequestered savant"])]
        martiallist = ["Victors eat the liver of foes slain in single combat", "Warriors tattoo the name of their blood foe on their sword arm",
                       "Warriors are forbidden to use " + random.choice(["missile weapons", "missile weapons", "shields", "shields", "two-handed weapons", "mounts"]),
                       "Upon his death, a warrior's deeds are carved into a stone pillar",
                       "Warriors " + random.choice(["shave their bodies", "shave their bodies", "add body art for each battle", "add body art for each battle", "practice self-mutilation", "practice self-mutilation",]),
                       "Warriors wear the " + random.choice(["ears", "eyes", "scalp", "fingers", "genitals", "teeth"]) + "of slain foes"]
        genderroleslist = ["Women chose their husband", "Wife may take multiple husbands",
                           "Women are " + random.choice(["officers of the court", "warriors", "clergy", "hunters", "sorcerers", "diplomats"]),
                           "Family line traced through mother",
                           "Only women may " + random.choice(["smoke", "be literate", "file legal suits", "bear shields", "distill alcohol", "handle money"]),
                           "women must cover " + random.choice(["face", "face", "arms", "arms", "legs", "ankles"]) + " in public",]
        lawlist = ["Criminals are " + random.choice(["formed into military units", "indentured to wealthy families", "forced to perform deadly work"]),
                   "Prohibition of " + random.choice(["alcohol", "meat", "prostitution", "long hair", "tea", "games of chance"]),
                   "Innocence of the accused determined by " + random.choice(["single combat", "single combat", "physical sport", "physical sport", "ordeal", "divination"]),
                   "It is legal to commit " + random.choice(["murder", "murder", "witchcraft", "rape", "theft", "usury"]),
                   "Criminals executed by " + random.choice(["ravenous insects", "gladiatorial combat", "starvation", "fatal parasite", "flaying", "planar banishment"]),
                   "Guilty verdicts overturned for " + random.choice(["money", "money", "completion of a quest", "assassinating a rival of the court", "relinquishing a slave to serve sentence", "self-mutilation"])]

        strangecustomlistoflists = [birthlist, riteofpassagelist, marriagelist, deathlist, rulershiplist, martiallist, genderroleslist, lawlist]
        for d4 in range(random.randint(1,4)):
            quirkRoll = diceSet.rollresultsclear(20,1)[0][0]
            if quirkRoll != 20:
                quirk = quirk + quirkList[quirkRoll-1] + random.choice(listofquirklists[quirkRoll-1]) + "\n"
            else:
                quirk = quirk + quirkList[quirkRoll-1] + random.choice(random.choice(strangecustomlistoflists)) + "\n"

        return "There is a " + typeandpop + ", ruled by: " + rulers + ", the government being: " + gov +\
               ", alignment being: " + alignment + ", primary commerce being: " + commerce + ", With the quirks of: \n" +\
                quirk







    def generateMap(self, numoftiles):
        diceSet = Dice()
        for x in range(numoftiles):
            hex = AtlasHex()
            terrainDict = self.primaryTerrainDictList[random.randint(0,6)]
            primaryTerrain = terrainDict["primary"]
            # Set primary terrain and surrounding terrain
            hex.setprimaryterrain(primaryTerrain)
            surroundingtiles = []
            for y in range(6):
                tile = ""
                terrainType = ""
                roll = diceSet.rollresultsclear(12, 1)[0][0]
                if roll <= 6:
                    terrainType = terrainDict["primary"]
                elif 6 < roll <= 9:
                    terrainType = terrainDict["secondary"]
                elif 9 < roll <= 11:
                    terrainType = terrainDict["tertiary"]
                else:
                    wildcardlist = terrainDict["wildcard"]
                    terrainType = wildcardlist[random.randint(0, len(wildcardlist)-1)]

                if primaryTerrain == "water" and terrainType == "forest":
                    if diceSet.rollresultsclear(100, 1)[0][0] <= 66:
                        tile = "light forest"
                        surroundingtiles.append(tile)
                    else:
                        surroundingtiles.append(terrainType)
                elif primaryTerrain == "desert" and terrainType == "hills":
                    if diceSet.rollresultsclear(100, 1)[0][0] <= 33:
                        tile = "rocky desert or high sand dunes"
                        surroundingtiles.append(tile)
                    else:
                        surroundingtiles.append(terrainType)
                elif primaryTerrain == "forest" and terrainType == "forest":
                    if diceSet.rollresultsclear(100, 1)[0][0] <= 33:
                        tile = "heavy forest"
                        surroundingtiles.append(tile)
                    else:
                        surroundingtiles.append(terrainType)
                elif primaryTerrain == "forest" and terrainType == "hills":
                    if diceSet.rollresultsclear(100, 1)[0][0] <= 66:
                        tile = "forested hills"
                        surroundingtiles.append(tile)
                    else:
                        surroundingtiles.append(terrainType)
                elif primaryTerrain == "forest" and terrainType == "mountains":
                    if diceSet.rollresultsclear(100, 1)[0][0] <= 66:
                        tile = "forested mountains"
                        surroundingtiles.append(tile)
                    else:
                        surroundingtiles.append(terrainType)
                elif primaryTerrain == "hills" and terrainType == "forest":
                    if diceSet.rollresultsclear(100, 1)[0][0] <= 33:
                        tile = "forested hills"
                        surroundingtiles.append(tile)
                    else:
                        surroundingtiles.append(terrainType)
                elif primaryTerrain == "hills" and terrainType == "hills":
                    if diceSet.rollresultsclear(100, 1)[0][0] <= 20:
                        tile = "canyon or fissure"
                        surroundingtiles.append(tile)
                    else:
                        surroundingtiles.append(terrainType)
                elif primaryTerrain == "hills" and terrainType == "mountains":
                    if diceSet.rollresultsclear(100, 1)[0][0] <= 40:
                        tile = "mountain pass"
                        surroundingtiles.append(tile)
                    else:
                        surroundingtiles.append(terrainType)
                elif primaryTerrain == "mountains" and terrainType == "forest":
                    if diceSet.rollresultsclear(100, 1)[0][0] <= 33:
                        tile = "forested mountain"
                        surroundingtiles.append(tile)
                    else:
                        surroundingtiles.append(terrainType)
                elif primaryTerrain == "mountains" and terrainType == "mountains":
                    if diceSet.rollresultsclear(100, 1)[0][0] <= 5:
                        tile = "volcano"
                        surroundingtiles.append(tile)
                    elif diceSet.rollresultsclear(100, 1)[0][0] <= 10:
                        tile = "mountain pass"
                        surroundingtiles.append(tile)
                    elif diceSet.rollresultsclear(100, 1)[0][0] <= 20:
                        tile = "dominating peak"
                        surroundingtiles.append(tile)
                    else:
                        surroundingtiles.append(terrainType)
                else:
                    surroundingtiles.append(terrainType)
            hex.setsurroundingsixehexes(surroundingtiles)
            self.hexList.append(hex)
            # End setting terrain
        #Major and minor event generator
        for hexagon in self.hexList:
            roll = diceSet.rollresultsclear(100, 1)[0][0]
            if roll <= self.majorminorchanceencounter[hexagon.getprimaryterrain()][0] + self.climatemodifier[self.climate]:
                majencounterroll = diceSet.rollresultsclear(6,1)[0][0]
                if majencounterroll == 1:
                    hexagon.setmajorencounter(self.generateSettlement())
                # elif majencounterroll == 2:
                #     #hexagon.setmajorencounter(self.generateFortress())
                # elif majencounterroll == 3:
                #     #hexagon.setmajorencounter(self.generateReligiousOrder())
                # elif majencounterroll == 4:
                #     #hexagon.setmajorencounter(self.generateRuin())
                # elif majencounterroll == 5:
                #     #hexagon.setmajorencounter(self.generateMonster())
                # elif majencounterroll == 6:
                #     #hexagon.setmajorencounter(self.generateNaturalPhenomenon())




    def setname(self, name):
        self.name = name

    def setclimate(self, climate):
        if climate in ["artic", "sub-artic", "temperate", "sub-tropical", "tropical"]:
            self.climate = climate
        else:
            print("Not a valid climate!")
    def getclimate(self):
        return self.climate

    def appendhextolist(self, hex):
        self.hexList.append(hex)
    def printmap(self):
        print(self.name)
        print("-------------------------------------------------------------------------------------------------------")
        print("Climate: " + self.climate)
        print("-------------------------------------------------------------------------------------------------------")
        hexIndex = 1
        for hex in self.hexList:

            print("-------------------------------------------------------------------------------------------------------")
            print(str(hexIndex))
            hex.printhex()
            print("-------------------------------------------------------------------------------------------------------")
            hexIndex = hexIndex + 1


map = Map()
map.setname("Testus")
map.setclimate("temperate")
map.generateMap(38)
map.printmap()


