# -*- coding: utf-8 -*-
import ast, random

chapter = ""
ng = ""
a = "stupid"
b = "stupid"
c = "stupid"
d = "stupid"
name = ""
counter = 0
contract = "LOOKING FOR ADVENTURERS! \nKia ora, we need your help to deliver some goods. We will pay you 100 gold to defend and deliver our goods to South MosesVille. We will provide you with a free travellers pack filled with all the goodies you need to survive the trip. "
minicontract = "deliver goods to South MosesVille for 100 gold"
southMosesVilleShortCut = "Head west to the Ancient Forests of Annagia. Climb largest tree next to the giant Mushroom. At the top there is a zip line you can take that will take you straight to South MosesVille. "
mapToSouthMosesVille = "Go to Ancient Forests of Annagia. Follow path 20km to South MosesVille. "

  
party = []

myStats = {
        "name": "",
        "Race": "",
        "Class":"",
        "Strength": 10,
        "Dexterity": 10,
        "Constitution": 10,
        "Intelligence": 10,
        "Wisdom": 10,
        "Charisma":10,
        "AttackCounter": 1,
        "Heal":5,
        "Stealth":3,
        "Armor":15,
        "Gold":10,
        "silver":0,
        "copper":0
        }

enemyStats = {
        "name": "",
        "Race": "Human",
        "Class":"None",
        "Strength": 10,
        "Dexterity": 10,
        "Constitution": 8,
        "Intelligence": 10,
        "Wisdom": 10,
        "Charisma":10,
        "AttackCounter": 1,
        "Heal":5,
        "Stealth":0,
        "Armor":10
        }

bag = {}

spellbook = {}

resistance = {}

attack = {
        "unarmed": 1,
        "short sword": 3
        }

def main():
    if(chapter == ""):
        title()
        getName()
    
    if(chapter == "0"):
        getRace()
        getClass()
        
    if(chapter == "1"):
        intro()
        
    if(chapter == "2"):
        testBattle()

    if(chapter == "3"):
        chapter3()

def title():
    print('Welcome to text adventures')
    contin = input("Do you want to start new game? \ny or n...")
    if(contin.lower() == "n"):
        contin = input("Insert character_name: ")
        load(contin)


def load(textfile):
    global myStats, spellbook ,bag, attack, resistance, chapter, party, ng
    
    statsString = textfile + "Stats.txt"
    bagString = textfile + "Bag.txt"
    spellbookString = textfile + "Book.txt"
    resistanceString = textfile + "Resistance.txt"
    attackString = textfile + "Attack.txt"
    chapterString = textfile + "Chapter.txt"
    partyString = textfile + "Party.txt"
    
    openfile = open(statsString)
    statsLoaded = openfile.read()
    openfile.close()
    myStats = ast.literal_eval(statsLoaded)
    
    openfile = open(bagString)
    bagLoaded = openfile.read()
    openfile.close()
    bag = ast.literal_eval(bagLoaded)
    
    openfile = open(spellbookString)
    spellbookLoaded = openfile.read()
    openfile.close()
    spellbook = ast.literal_eval(spellbookLoaded)
    
    openfile = open(resistanceString)
    resistanceLoaded = openfile.read()
    openfile.close()
    resistance = ast.literal_eval(resistanceLoaded)
    
    openfile = open(attackString)
    attackLoaded = openfile.read()
    openfile.close()
    attack = ast.literal_eval(attackLoaded)
    
    openfile = open(chapterString)
    chapterLoaded = openfile.read()
    openfile.close()
    chapter = chapterLoaded
    
    openfile = open(partyString)
    partyLoaded = openfile.read()
    openfile.close()
    party = partyLoaded.split()
    
    if(ng == ""):
        print("Stats:",myStats)
        print("Attacks and weapons:",attack)
        print("Chapter =",chapter)
        print("Party:",party)
        ng = "stop"

def save(textfile):
    global myStats,spellbook,bag,attack,resistance,chapter,party
    
    statsString = textfile + "Stats.txt"
    newmyStats = str(myStats)
    bagString = textfile + "Bag.txt"
    newspellbook = str(spellbook)
    spellbookString = textfile + "Book.txt"
    newbag = str(bag)
    resistanceString = textfile + "Resistance.txt"
    newattack = str(attack)
    attackString = textfile + "Attack.txt"
    newresistance = str(resistance)
    chapterString = textfile + "Chapter.txt"
    partyString = textfile + "Party.txt"
    newparty = "".join(str(x) for x in party)
    
    write = open(statsString,'w')
    write.write(newmyStats)
    write.close()
    
    write = open(bagString,'w')
    write.write(newbag)
    write.close()
    
    write = open(spellbookString,'w')
    write.write(newspellbook)
    write.close()
    
    write = open(resistanceString,'w')
    write.write(newresistance)
    write.close()
    
    write = open(attackString,'w')
    write.write(newattack)
    write.close()
    
    write = open(chapterString,'w')
    write.write(chapter)
    write.close()
    
    write = open(partyString,'w')
    write.write(newparty)
    write.close()
    
    load(textfile)
    
def getName():
    global chapter, myStats
    name = input('Hello adventurer! What is your name? ')
    if(name == "exit"):
        raise SystemExit
    print('Aaaah,', name, 'was it?')
    reply = input("y or n? ")
    if (reply == 'y'):
        myStats.update({"name":name})
    else:
        name = input('Enter your name again: ')
        print('Very well', name,) 
        input("shall we continue?..")
        myStats.update({"name":name})
    chapter = "0"
    if("silverd" in name.lower()):
        myStats = {
        "name": "Silverdangdogdiggitydelldave",
        "Race": "Mexican",
        "Class":"Cow boy",
        "Strength": 12,
        "Dexterity": 12,
        "Constitution": 12,
        "Intelligence": 12,
        "Wisdom": 12,
        "Charisma":12,
        "AttackCounter": 1,
        "Heal":7,
        "Stealth":5,
        "Armor":16,
        "Gold":0,
        "silver":420,
        "copper":0
        }
        chapter = "2"
        party.append("Ryuga ")
        bag["mapToSouthMosesVille"] = mapToSouthMosesVille
        attack["Death Blade"] = 10
        spellbook["Spirit bomb"] = 12
        save(myStats["name"])


    
def getRace():
    global a
    if(a == "stupid"):
        print("Now",myStats["name"], ", there are 3 different races to choose from")
        input("There are the dragonborn, a mighty race who excell in strength and charisma...")
        input("Elves who excell in intelligence and dexterity...")
        input("and dwarves who excell in wisdom and constitution...")
        a = "notStupid"
    raceReply = input("Which would you like to be? \nA)Dragonborn \nB)Elf \nC)Dwarf\nD)See description again\n...")
    
    if(raceReply.lower() == 'a'or raceReply.lower() == 'dragonborn'):
        myStats.update({'Race': "Dragonborn"})
        myStats["Strength"] = myStats["Strength"] + 2
        myStats["Charisma"] = myStats["Charisma"] + 2
        resistance["full"] = "fire"
        attack.update({'unarmed': 3})
        attack["dragon breath"] = 4
        input("Amazing, I have never met a dragonborn in person before. A dragonborn of your size must be exetremely powerful!..")
        input("--- gained resistance to fire ---")
        input("--- gained dragon breath ---")
        
    elif(raceReply.lower() == 'b' or raceReply.lower() == 'elf' or raceReply.lower() == 'e'):
        myStats.update({'Race': "Elf"})
        myStats["Intelligence"] = myStats["Intelligence"] + 2
        myStats["Dexterity"] = myStats["Dexterity"] + 2
        attack[" short bow"] = 4
        input("Holy balls, you're the tallest elf I have ever seen?! Spectacular, I heard your kind are very skilled archers...")
        input("Here take this short bow, I have no use for it...")
        input("--- gained short bow ---")
        
    elif(raceReply.lower() == 'c' or raceReply.lower() == 'dwarf'):
        myStats.update({'Race': "Dwarf"})
        myStats["Constitution"] = myStats["Constitution"] + 2
        myStats["Wisdom"] = myStats["Wisdom"] + 2
        myStats["Heal"] = myStats["Heal"] + 2
        attack["battle axe"] = 4
        input("Aaah a fellow dwarf. Here take my trusty battle axe for your travels...")
        input("--- gained battle axe ---")
    
    elif(raceReply.lower() == 'd'):
        a = "stupid"
        getRace()
        
    elif(raceReply.lower() == 'options' or raceReply.lower() == 'stats' or raceReply.lower() == 'o' or raceReply.lower() == 's'):
        options()
        getRace()
        
    else:
        getRace()
    
def getClass():
    global b,chapter,ng
    if(b == "stupid"):
        input("Along with races, you can also choose a class. You have 3 more to choose from...")
        input("Monks, they have mastered the art of their body and are tremendous in hand to hand combat...")
        input("Rogues, they are sneaky, agile and very nimble. They are experts in stealth...")
        input("And sorcerers, while weak in melee combat they exceed in mid-long range combat. They are masters of arcane magic and have access to a multitude of powerful spells...")
        b = "notStupid"
    classReply = input("Which would you like to be? \nA)Monk \nB)Rogue \nC)Sorcerer \nD)See description again\n...")
    
    if(classReply.lower() == 'a' or classReply.lower() == 'm'):
        myStats.update({'Class': "Monk"})
        attack.update({'unarmed': 4})
        myStats.update({'AttackCounter': 2})
        input("Who would have though you were a monk. Wowzers, did you know you could make two unarmed attack each round?..")
        input("--- gained second attack ---")
        
    elif(classReply.lower() == 'b' or classReply.lower() == 'r'):
        myStats.update({'Class': "Rogue"})
        myStats.update({'Stealth': 2})
        attack["stealth attack"] = 5
        input("So you are one of them? Im not surprised, I'll be keeping a close eye on you. Anyways, did you know you could make an attack from stealth to do more damage?..")
        input("im sure you did. \n--- gained stealth attack ---")
    
    elif(classReply.lower() == 'c' or classReply.lower() == 's'):
        myStats.update({'Class': "Sorcerer"})
        sorcererReply = input("A sorcerer, hmmm interesting. do you have spell book? \ny or n? ")
        if(sorcererReply == 'y'):
            spellbook["firebolt"] = 6
            input("Excellent, take this...")
            input("--- gained fire bolt ---")

        else:
            spellbook["burning hands"] = 10
            spellbook["firebolt"] = 6
            input("Im sure I have one lying around somewhere...")
            input("Oh here it is, take this...")
            input("--- gained spell book with fire bolt and burning hands ---")
                
        
    elif(classReply.lower() == 'd'):
        b = "stupid"
        getClass()
        
    elif(classReply.lower() == 'options'or classReply.lower() == 'stats' or classReply.lower() == 'o' or classReply.lower() == 's'):
        options()
        getClass()
        
    else:
        getClass()
    
    reply = input("Are you sure you want to be a {}, {}. \ny or n... ".format(myStats["Race"],myStats["Class"]))
    if(reply.lower() == "n"):
        main()

    chapter = "1"
    ng = "stop"
    save(myStats["name"])


def intro():    
    global c,counter,contract, chapter, ng
    if(c == "stupid"):
        input("~Chapter 1 - Game of y and n? ~")
        input("???: Howdy partner, my name is Silverdangdogdiggitydelldave the second, but you can just call me Silverdangdogdiggitydelldave. It's a lot more convinient for others ya know...")
        input("Silverdangdogdiggitydelldave: So I hear you're an adventurer. Don't really look like an adventurer but I guess im supposed to give you this...")
        bag["Contract"] = minicontract
        input("--- Received contract ---")    
        c = "notStupid"
    if(counter == 2):
        input("Silverdangdogdiggitydelldave: *SIGH* Give it here")
        reply = 'y'
    else:        
        reply = str(input("Will you read it? \ny or n... "))   
        
    if(reply.lower() == 'y' or reply.lower() == "yes" or reply.lower() == "ya" or reply.lower() == "yup" or reply.lower() == "ok" or reply.lower() == "okay" or reply.lower() == "sure" or reply.lower() == "yeah" or reply.lower() == "mhmm" or reply.lower() == "mmm"):
        input(contract)
        input("Silverdangdogdiggitydelldave: I bet that's more gold then you've ever laid eyes on hahaa-ha, yeah me too...")
        input("Silverdangdogdiggitydelldave: I used to live in South MosesVille, or was it opposite South MosesVille, I forget. But if things haven't changed it's the safest ville of them all...")
        print("Silverdangdogdiggitydelldave: I think you should definitely go, a strong",myStats["Race"],"like yourself shouldn't have anything to worry about")
        reply = str(input("Will you accept contract? \ny or n... "))
        if(reply.lower() == 'y' or reply.lower() == "yes" or reply.lower() == "ya" or reply.lower() == "yup" or reply.lower() == "ok" or reply.lower() == "okay" or reply.lower() == "sure" or reply.lower() == "yeah" or reply.lower() == "mhmm" or reply.lower() == "mmm"):
            input("Silverdangdogdiggitydelldave: If you're scared you can always look for a party to go with and split the gold...")
            reply = input("Do you want to find a party to travel with? \ny or n...")
            if(reply.lower() == 'y' or reply.lower() == "yes" or reply.lower() == "ya" or reply.lower() == "yup" or reply.lower() == "ok" or reply.lower() == "okay" or reply.lower() == "sure" or reply.lower() == "yeah" or reply.lower() == "mhmm" or reply.lower() == "mmm"):
                if(myStats["Race"] == "Dragonborn"):
                    party.append("Goku ")
                    input("You accepted the contract and found 1 party member willing to travel with you...")
                    input("--- Obtained travellers pack ---")
                    bag["Contract"] = minicontract
                    chapter = "2"
                    ng = "stop"
                    save(myStats["name"])
                elif(myStats["Race"] == "Elf"):
                    party.append("Andy ")
                    party.append("Randy ")
                    party.append("Mandy ")
                    input("You accepted the contract and found 3 party members willing to travel with you...")
                    input("--- Obtained travellers pack ---")
                    bag["Contract"] = minicontract
                    chapter = "2"
                    ng = "stop"
                    save(myStats["name"])
                else:
                    party.append("Rachel ")
                    party.append("Delme ")
                    input("You accepted the contract and found 2 party members willing to travel with you...")
                    input("--- Obtained travellers pack ---")
                    bag["Contract"] = minicontract
                    chapter = "2"
                    ng = "stop"
                    save(myStats["name"])
            else:
                input("You accepted the contract. You are also an independant solo player who doesnt need no party members...")
                input("--- Obtained travellers pack ---")
                bag["Contract"] = minicontract
                chapter = "2"
                ng = "stop"
                save(myStats["name"])
        else:
            party.append("Silverdangdogdiggitydelldave ")
            input("You know what, leeeets go partner, You and I will make the best party together. We'll split the gold, it'll be great...")
            input("I'll go pack my stuff and meet you out front :)")
            input("You accepted the contract and partied up with Silverdangdogdiggitydelldave...")
            input("--- Obtained travellers pack ---")
            bag["Contract"] = minicontract
            chapter = "2"
            ng = "stop"
            save(myStats["name"])
            
    elif(reply.lower() == "n" and counter < 2):
        print("Try entering 'hell naah' or 'you read it' \nYou should probably read it pal!..")
        counter += 1
        intro()
    elif(reply.lower() == "no"  and counter < 2):
        print("Do you need help reading it?")
        counter += 1
        intro()
    elif(reply.lower() == "hell naah"  and counter < 2):
        print("Loooooking f-f-f-for a-a-a-ad.")
        counter += 1
        intro()
    elif(reply.lower() == "you read it"  and counter < 2):
        input("You will go far in this game...")
        input("Or will you?..")
        myStats["Intelligence"] = myStats["Intelligence"] + 2
        input("--- Intelligence increased by 2 ---")
        counter = 2
        intro()
    else:
        print("I'd suggest taking a look at that.")
        counter += 1
        intro()
    
def testBattle():
    global d, chapter, ng
    if(d == "stupid"):
        d = "notStupid"
        input("~Chapter 2 - First encounter ~")
    
    if(not party):
        input("Maybe I should test my skills before I go to South MosesVille...")
        reply = input("A)Ask people to spar \nB)Look for a challenge \nC)Naah I don't need it \n...")
        if(reply.lower() == 'a'):
            input("Hey you, big guy! You wanna do some light sparring?")
            input("???: Who me?")
            input("No I was actually talking about the guy over there but I guess you'll do")
            input("???: Are you trying to call me small?! \nI'll kick your head in!!")
            input("Hey man calm down...")
            input("???: I'LL SHOW YOU THE TRUE POWER OF SILVERDANGDOGDIGGITYDELLDAVE THE THIRD!!!1!")
            input("You have got to be kidding me")
            input("Get ready for your first fight.")
            winner = oneVsOneFight("Silverdangdogdiggitydelldave the third",20,0)
            input("{} won the battle".format(winner))
            if(winner == myStats["name"]):
                input("Silverdangdogdiggitydelldave the third: Jesus, you are a lot stronger then you look. I'll get you next time...")
                input("Silverdangdogdiggitydelldave the third: So what brings you here? I don't think I have seen you before?..")
                while(d == "notStupid"):
                    reply = input("A)I'm just an adventurer passing through town \nB)The real question is, what brings you here? I don't think I have seen you before? \n..")
                    if(reply.lower() == "a"):
                        input("Silverdangdogdiggitydelldave the third: An adventurer you say? Where are you going?")
                        reply = input("A)Whats it to ya? \nB)The real question is, where are yooou going? \nC)Im going to South MosesVille.\n..")
                        if(reply.lower() == "a"):
                            input("Silverdangdogdiggitydelldave the third: Just curious...")
                            input("Please don't talk to me weakling")
                        elif(reply.lower() == "b"):
                            input("Silverdangdogdiggitydelldave the third: haha I like you...")
                            input("Silverdangdogdiggitydelldave the third: I'm going to South MosesVille...")
                            input("yikes, yeah me too...")
                            input("Silverdangdogdiggitydelldave the third: Hey why don't you come with me, I know a really good short cut...")
                            reply = input("A)Sure thing \nB)I think i'll be okay \nC)Sorry but i'm a solo player\n..")
                            if(reply.lower() == "a"):
                                party.append("SilverdangdogdiggitydelldaveIII ")
                                input("We can take the extra fast way with your strength...")
                                input("--- New party member ---")
                            elif(reply.lower() == "b"):
                                party.append("SilverdangdogdiggitydelldaveIII ")
                                input("Silverdangdogdiggitydelldave the third: You know what, lets f**cking goooo! We'll just travel together to South MosesVille, it'll be great!")
                                input("Silverdangdogdiggitydelldave the third: We can take the extra fast way with your strength...")
                                input("--- New party member ---")
                            else:
                                input("Silverdangdogdiggitydelldave the third: I respect that, you sound just like my buddy Kirito \n I'm sure you two would have got along well")
                                input("Silverdangdogdiggitydelldave the third: Well safe travels, maybe I will see you in South MosesVille")
                                input("Silverdangdogdiggitydelldave the third: If you want to take the shortcut, heres a map I made with directions...")
                                input("--- Gained map to South MosesVille ---")
                                bag["SouthMosesVilleMap"] = southMosesVilleShortCut
                        else:
                            input("Silverdangdogdiggitydelldave the third: Oh no way hombre, me too. Lets party up, I know a shortcut there...")
                            reply = input("A)Tell me more about this shortcut \nB)Hell naah \nC)Sorry but i'm a solo player\n..")
                            if(reply.lower() == "a"):
                                party.append("SilverdangdogdiggitydelldaveIII ")
                                input("Silverdangdogdiggitydelldave the third: Well what is there to say. 'An alternative root(route) that is shorter than the one usually taken. - google'")
                                input("Silverdangdogdiggitydelldave the third: I'll show you...")
                                input("--- New party member ---")
                            elif(reply.lower() == "b"):
                                input("Silverdangdogdiggitydelldave the third: WOW!..")
                                input("Silverdangdogdiggitydelldave the third: RUDE!!! You might be stronger then me but my dad will put you in your place you runt")
                                input("Silverdangdogdiggitydelldave the third: Oh hey Dad, I didn't see you there \n This {} beat me up".format(myStats["Race"]))
                                input("Silverdangdogdiggitydelldave the second: Go home bronzedangdogdiggitydelldave, and stop calling me dad. \nYou're adopted...")
                                input("Welp... *awkward silence* \n I'm gonna leave")
                                input("Silverdangdogdiggitydelldave the second: Hey wait, I forgot to give you this...")
                                input("--- Gained map to South MosesVille ---")
                                bag["SouthMosesVilleMap"] = mapToSouthMosesVille
                            else:
                                input("Silverdangdogdiggitydelldave the third: I respect that, you sound just like my buddy Kirito \n I'm sure you two would have gotten along")
                                input("Silverdangdogdiggitydelldave the third: Well safe travels, maybe I will see you in South MosesVille")
                                input("Silverdangdogdiggitydelldave the third: If you want to take the shortcut, heres a map I made with directions...")
                                input("--- Gained map to South MosesVille ---")
                                input("Kirito?!. Hmmm \nMaybe I should ask Silverdangdogdiggitydelldave the second about him... ")
                                bag["SouthMosesVilleMap"] = southMosesVilleShortCut
                        break

                    elif(reply.lower() == "b"):
                        input("Silverdangdogdiggitydelldave the third: Wow, I didn't know you were a troll. Could have sworn you were a {}.".format(myStats["Race"]))
                        input("Hahahaha. Halrious, call me a troll again and it'll be the last thing you say!")
                        input(".......")
                        input("Silverdangdogdiggitydelldave the second: Hello {}. \nI see you have met Golddangdogdiggitydelldave, my adapted son ".format(myStats["name"]))
                        input("Oh shit, how long have you been standing there?..")
                        input("Silverdangdogdiggitydelldave the second: I just came to give you something but after this act of bullying I think I'll keep it for myself")
                        break
                    
                    else:
                        input("Invalid Answer...")
            else:
                input("I can't believe I lost")
                input("Silverdangdogdiggitydelldave the third: Hey, don't beat yourself up, it was a tough fight and you came really close to winning but in the end I am the greatest fighter ever hehehe.")  
                input("Maybe I'm not cut out for an adventurer. \nMaybe I'm not ready...")
                if(myStats["Class"] == "Rogue"):
                    input("Silverdangdogdiggitydelldave the third: {}, You gotta believe in yourself, Cause that's your ninja way.\nBelieve it".format(myStats["Class"]))
                input("Silverdangdogdiggitydelldave the third: So what brings you here? I don't think I have seen you before?..")
                while(d == "notStupid"):
                    reply = input("A)I'm just an adventurer passing through town \nB)The real question is, what brings you here? I don't think I have seen you before? \n..")
                    if(reply.lower() == "a"):
                        input("Silverdangdogdiggitydelldave the third: An adventurer you say? Where are you going?")
                        reply = input("A)Whats it to ya? \nB)The real question is, where are yooou going? \nC)Im going to South MosesVille.\n..")
                        if(reply.lower() == "a"):
                            input("Silverdangdogdiggitydelldave the third: Just curious...")
                            input("I'm going to South MosesVille")
                            input("Silverdangdogdiggitydelldave the third: Oh no way hombre, me too. Lets party up, I know a shortcut there...")
                            reply = input("A)Tell me more about this shortcut \nB)Hell naah \nC)Sorry but i'm a solo player\n..")
                            if(reply.lower() == "a"):
                                party.append("SilverdangdogdiggitydelldaveIII ")
                                input("Silverdangdogdiggitydelldave the third: Well what is there to say. 'An alternative root(route) that is shorter than the one usually taken. - google'")
                                input("Silverdangdogdiggitydelldave the third: I'll show you...")
                                input("--- New party member ---")
                            elif(reply.lower() == "b"):
                                input("Silverdangdogdiggitydelldave the third: WOW!..")
                                input("Silverdangdogdiggitydelldave the third: RUDE!!! You might be stronger then me but my dad will put you in your place you runt")
                                input("Silverdangdogdiggitydelldave the third: Oh hey Dad, I didn't see you there \n This {} beat me up".format(myStats["Race"]))
                                input("Silverdangdogdiggitydelldave the second: Go home bronzedangdogdiggitydelldave, and stop calling me dad. \nYou're adopted...")
                                input("Welp... *awkward silence* \n I'm gonna leave")
                                input("Silverdangdogdiggitydelldave the second: Hey wait, I forgot to give you this...")
                                input("--- Gained map to South MosesVille ---")
                                bag["SouthMosesVilleMap"] = mapToSouthMosesVille
                            else:
                                input("Silverdangdogdiggitydelldave the third: I respect that, you sound just like my buddy Kirito \n I'm sure you two would have gotten along")
                                input("Silverdangdogdiggitydelldave the third: Well safe travels, maybe I will see you in South MosesVille")
                                input("Silverdangdogdiggitydelldave the third: If you want to take the shortcut, heres a map I made with directions...")
                                input("--- Gained map to South MosesVille ---")
                                input("Kirito?!. Hmmm \nMaybe I should ask Silverdangdogdiggitydelldave the second about him... ")
                                bag["SouthMosesVilleMap"] = southMosesVilleShortCut

                        elif(reply.lower() == "b"):
                            input("Silverdangdogdiggitydelldave the third: haha I like you...")
                            input("Silverdangdogdiggitydelldave the third: I'm going to South MosesVille...")
                            input("yikes, yeah me too...")
                            input("Silverdangdogdiggitydelldave the third: Hey why don't you come with me, I know a really good short cut...")
                            reply = input("A)Sure thing \nB)I think i'll be okay \nC)Sorry but i'm a solo player\n..")
                            if(reply.lower() == "a"):
                                party.append("SilverdangdogdiggitydelldaveIII ")
                                input("We can take the extra fast way with your strength...")
                                input("--- New party member ---")
                            elif(reply.lower() == "b"):
                                party.append("SilverdangdogdiggitydelldaveIII ")
                                input("Silverdangdogdiggitydelldave the third: You know what, lets f**cking goooo! We'll just travel together to South MosesVille, it'll be great!")
                                input("Silverdangdogdiggitydelldave the third: We can take the extra fast way with your strength...")
                                input("--- New party member ---")
                            else:
                                input("Silverdangdogdiggitydelldave the third: I respect that, you sound just like my buddy Kirito \n I'm sure you two would have got along well")
                                input("Silverdangdogdiggitydelldave the third: Well safe travels, maybe I will see you in South MosesVille")
                                input("Silverdangdogdiggitydelldave the third: If you want to take the shortcut, heres a map I made with directions...")
                                input("--- Gained map to South MosesVille ---")
                                bag["SouthMosesVilleMap"] = southMosesVilleShortCut
                        else:
                            input("Silverdangdogdiggitydelldave the third: Oh no way hombre, me too. Lets party up, I know a shortcut there...")
                            reply = input("A)Tell me more about this shortcut \nB)Hell naah \nC)Sorry but i'm a solo player\n..")
                            if(reply.lower() == "a"):
                                party.append("SilverdangdogdiggitydelldaveIII ")
                                input("Silverdangdogdiggitydelldave the third: Well what is there to say. 'An alternative root(route) that is shorter than the one usually taken. - google'")
                                input("Silverdangdogdiggitydelldave the third: I'll show you...")
                                input("--- New party member ---")
                            elif(reply.lower() == "b"):
                                input("Silverdangdogdiggitydelldave the third: WOW!..")
                                input("Silverdangdogdiggitydelldave the third: RUDE!!! You might be stronger then me but my dad will put you in your place you runt")
                                input("Silverdangdogdiggitydelldave the third: Oh hey Dad, I didn't see you there \n This {} beat me up".format(myStats["Race"]))
                                input("Silverdangdogdiggitydelldave the second: Go home bronzedangdogdiggitydelldave, and stop calling me dad. \nYou're adopted...")
                                input("Welp... *awkward silence* \n I'm gonna leave")
                                input("Silverdangdogdiggitydelldave the second: Hey wait, I forgot to give you this...")
                                input("--- Gained map to South MosesVille ---")
                                bag["SouthMosesVilleMap"] = mapToSouthMosesVille
                            else:
                                input("Silverdangdogdiggitydelldave the third: I respect that, you sound just like my buddy Kirito \n I'm sure you two would have gotten along")
                                input("Silverdangdogdiggitydelldave the third: Well safe travels, maybe I will see you in South MosesVille")
                                input("Silverdangdogdiggitydelldave the third: If you want to take the shortcut, heres a map I made with directions...")
                                input("--- Gained map to South MosesVille ---")
                                input("Kirito?!. Hmmm \nMaybe I should ask Silverdangdogdiggitydelldave the second about him... ")
                                bag["SouthMosesVilleMap"] = southMosesVilleShortCut
                        break

                    elif(reply.lower() == "b"):
                        input("Silverdangdogdiggitydelldave the third: Wow, I didn't know you were a troll. Could have sworn you were a {}.".format(myStats["Racee"]))
                        input("Hahahaha. Halrious, call me a troll again and it'll be the last thing you say!")
                        input(".......")
                        input("Silverdangdogdiggitydelldave the second: Hello {}. \nI see you have met Golddangdogdiggitydelldave, my adapted son ".format(myStats["name"]))
                        input("Oh shit, how long have you been standing there?..")
                        input("Silverdangdogdiggitydelldave the second: I just came to give you something but after this act of bullying I think I'll keep it for myself")
                        break
                    
                    else:
                        input("Invalid Answer...")
                
        elif(reply.lower() == 'b'):
            input("You see a large forest to the west and large mountains to your east.\nWhich would you like to investigate...")
            reply = input("A)Forest \nB)Mountains \n... ")
            if(reply.lower() == 'a'):
                input("You walked towards the forest and see a path. You can see a small goblin practicing thai chi.")
                reply = input("Do you approach him? \ny or n... ")
                if(reply.lower() == 'y'):
                    input("Goblin: I can see you there. Please don't attack me, I'm friendly")
                    reply = input("Do you trust him? \ny or n... ")
                    if(reply.lower() == 'y'):
                        input("Don't worry Goblin, im just looking to train")
                        input("Goblin: To train? What for?\nYou must be one of those adventurers right?")
                        input("Goblin: Can you help me out, I can give you some silver")
                        reply = input("A)Silver? How much silver?\nB)No sorry, I don't have any time for that\nC)*Walk closer* \n... ")
                        if(reply.lower() == 'a'):
                            input("Goblin: Well, to be fare I don't have much but I can give you 10 silver pieces.")
                            input("Goblin: All you have to do is help me pick these plants. I need 10 more. \n*Shows you plant*")
                            reply = input("Goblin: So will you help me? \ny or n. ")
                            if(reply.lower() == 'y'):
                                input("Hmm, this seems to be the one")
                                input("*Coughing* What's going on?")
                                input("Goblin: Mwahahahaha, silly {}, you fell right for my trap..".format(myStats["Race"]))
                                input("Goblin: That's actually a paralasis plant you fool, and I'm the only one with the antedote...")
                                input("Goblin: Now give me all your money or I'll leave you here to die..")
                                reply = input("A)Give money \nB)Attempt to fight")
                                if(reply.lower() == 'a'):
                                    myStats["Gold"] = 0
                                    input("Ok here, take everything I have")
                                    input(" --- You gave all your gold ---")
                                else:
                                    input("You think this is enough to paralyse me!? If so then you are the true fool")
                                    input("Lets Fight!")
                                    winner = oneVsOneFight("Goblin",20,0)
                                    if(winner == "Goblin"):
                                        input("GAME OVER")
                                        reply = input("Do you want to load game? \n y or n... ")
                                        if(reply.lower() == "y"):
                                            name = str(myStats["name"])
                                            load(name)
                                            main()
                                            raise SystemExit
                                    else:
                                        input("*You jump on top of the lifeless goblin and maul him long after he has died*... ")
                                        input("*You fall unconcious*... ")
                                        input("--- You were found by a guard who returned you to a hospital ---")
                                        input("*You wake up next to a masked man*")
                                        reply = input("A)Did you save me? \nB)Who are you? \nC)......\n...")
                                        if(reply.lower() == 'a'):
                                            input("???: Yes, I found you passed out next to a dead goblin. When you recover you will heading straight to prison...")
                                            input("PRISON??! He poisoned me and then tried to take advantage of me, I was barely able to protect myself..")
                                            input("???: Tell that to the judge")
                                            input("Silverdangdogdiggitydelldave: Hey, I heard you were found passed out in the Ancient forest of Annagia. I figured you had touched the parasalsis plant. I'm glad you got out okay. I probably should have given you this map to South MosesVille and told you about that  ...")
                                            input("--- Gained map to South MosesVille ---")
                                            input("Also don't worry about prison, I'll explain the situation to the mayor, I'm sure she'll understand")
                                            bag["SouthMosesVilleMap"] = mapToSouthMosesVille
                                        elif(reply.lower() == 'b'):
                                            input("???: I'm the gaurd who saved your life")
                                            input("Guard: But don't think you are going to be let out scot-free, I found a freshly killed goblin right next to you!")
                                            input("Silverdangdogdiggitydelldave: Hey, I heard you were found passed out in the Ancient forest of Annagia. I figured you had touched the parasalsis plant. I'm glad you got out okay. I probably should have given you this map to South MosesVille and told you about that  ...")
                                            input("--- Gained map to South MosesVille ---")
                                            input("Also don't worry about prison, I'll explain the situation to the mayor, I'm sure she'll understand")
                                            bag["SouthMosesVilleMap"] = mapToSouthMosesVille
                                        else:
                                            input("Mayor: Hello {}, I have been asked by Silverdangdogdiggitydelldave the second to come visit you!..".format(myStats["name"]))
                                            input("Mayor: Normally I wouldn't fufill sucha request, but for my brother, it's hard to say no...")
                                            input("Mayor: He also asked me to give you a map to South MosesVille, so here it is...")
                                            input("--- Gained map to South MosesVille ---")
                                            input("Mayor: Gaurd! You can leave, your work here is done. Rest up sweet prince, you will need it for your adventure to South Mosesville...")
                                            input("Gaurd: Yes sir...")
                                            input("Thank you...")
                                            bag["SouthMosesVilleMap"] = mapToSouthMosesVille
                            else:
                                input("I would never waste so much time to pick flowers for a lower class race like a Goblin... ")
                                input("I came to fight so prepare yourself maggot!..")
                                input("Lets Fight!")
                                winner = oneVsOneFight("Goblin",20,0)
                                if(winner == "Goblin"):
                                    input("I-I-I-I LOST...")
                                    input("GAME OVER")
                                    reply = input("Do you want to load game? \n y or n... ")
                                    if(reply.lower() == "y"):
                                        name = str(myStats["name"])
                                        load(name)
                                        main()
                                        raise SystemExit
                                else:
                                    input("Goblin: Please spare my life, I'll do anything. I just wanted help to gather these flowers")
                                    input("YOU ARE STILL TRYING TO TRICK ME INTO GATHERING THE PARALASIS PLANTS???!!")
                                    input("Goblin: H-h-how did you know what they were?..")
                                    input("*Stomps goblins head crushing his skull into pieces*")
                                    input("--- You now have a pure hatred towards all goblins ---")
                        elif(reply.lower() == 'b'):
                            input("Goblin: Oh come on man, give a brother a hand...")
                            input("A brother?? A lowly Goblin like yourself has no right to call me your brother...")
                            input("Now leave this forest before I end you right here!..")
                            input("Goblin: You will regret your decision to oppose me!..")
                            input("I'll get you...")
                            winner = oneVsOneFight("Goblin",20,0)
                            if(winner == "Goblin"):
                                input("I-I-I-I LOST...")
                                input("GAME OVER")
                                reply = input("Do you want to load game? \n y or n... ")
                                if(reply.lower() == "y"):
                                    name = str(myStats["name"])
                                    load(name)
                                    main()
                                    raise SystemExit
                            else:
                                input("I'll let you live so you can tell all the other Goblins out there not to mess with me...")
                                input("I will restore my honor and someday become the firelord!..")
                                input("Goblin: Thank you {}, I shall remember you as the adventurer who spared the life of a goblin...".format(myStats["Class"]))
                                input("Remember the name {}...".format(myStats["name"]))
                        else:
                            input("Goblin: Hey, stay right there. Don't come any closer...")
                            input("Goblin: Stop, please...")
                            reply = input("What will you do? \nA)Continue walking forward \nB)Talk to him \nC)Charge at him recklessly \n... ")
                            if(reply.lower() == 'a'):
                                input("Goblin: If it's a fight you want it's a fight you're going to get...")
                                input("Don't mess with me!..")
                                winner = oneVsOneFight("Goblin",20,0)
                                if(winner == "Goblin"):
                                    input("I-I-I-I LOST...")
                                    input("GAME OVER")
                                    reply = input("Do you want to load game? \n y or n... ")
                                    if(reply.lower() == "y"):
                                        name = str(myStats["name"])
                                        load(name)
                                        main()
                                        raise SystemExit
                                else:
                                    input("I'll let you live so you can tell all the other Goblins out there not to mess with me...")
                                    input("I will restore my honor and someday become the firelord!..")
                                    input("Goblin: Thank you {}, I shall remember you as the adventurer who spared the life of a goblin...".format(myStats["Class"]))
                                    input("Remember the name {}...".format(myStats["name"]))
                            elif(reply.lower() == 'b'):
                                input("Unless someone makes the first move, nothing will happen...")
                                input("Goblin: Wh-what do you plan on doing?...")
                                input("In the end, there is no greater motivation than revenge")
                                input("*Walks closer*")
                                input("Goblin: Wh-what are talking about. Revenge??.")
                                input("In this world, there is only good and evil...")
                                input("that was the first universal truth I grasped from observing the world around me when I was a child.")
                                input("Every human being without exception ends up falling into one category or the other.")
                                input("Goblin: *Charges at you...*")
                                input("I'll get you...")
                                winner = oneVsOneFight("Goblin",20,0)
                                if(winner == "Goblin"):
                                    input("I-I-I-I LOST...")
                                    input("GAME OVER")
                                    reply = input("Do you want to load game? \n y or n... ")
                                    if(reply.lower() == "y"):
                                        name = str(myStats["name"])
                                        load(name)
                                        main()
                                        raise SystemExit
                                    else:
                                        raise SystemExit
                                else:
                                    input("Sakujo....")
                                    input("Sakujoo....")
                                    input("SAKUJOOOOOO....")
                                    input("*After being brutally attacked the goblin suffered a heart attack*")
                            else:
                                ("*You go to charge at goblin but he begins to charge at you*")
                                input("Come at me like your life depends on it!")
                                input("Get ready for the next battle")
                                winner = oneVsOneFight("Goblin",20,0)
                                if(winner == "Goblin"):
                                    input("I-I-I-I LOST...")
                                    input("DEFEAT!")
                                    reply = input("Continue? \n y or n... ")
                                    if(reply.lower() == "y"):
                                        name = str(myStats["name"])
                                        load(name)
                                        main()
                                        raise SystemExit
                                    else:
                                        raise SystemExit
                                else:
                                    input("Your strength mirrors a child's beguilement...")
                                    input("Goblin: *Takes final break*")
                                    input("Weaklings should perish...")
            elif(reply.lower() == 'b'):
                input("You walked towards the mountains and see a path. You can see a small goblin practicing thai chi.")
                reply = input("Do you approach him? \ny or n... ")
                if(reply.lower() == 'y'):
                    input("Goblin: I can see you there. Please don't attack me, I'm friendly")
                    reply = input("Do you trust him? \ny or n... ")
                    if(reply.lower() == 'y'):
                        input("Don't worry Goblin, im just looking to train")
                        input("Goblin: To train? What for?\nYou must be one of those adventurers right?")
                        input("Goblin: Can you help me out, I can give you some silver")
                        reply = input("A)Silver? How much silver?\nB)No sorry, I don't have any time for that\nC)*Walk closer* \n... ")
                        if(reply.lower() == 'a'):
                            input("Goblin: Well, to be fare I don't have much but I can give you 10 silver pieces.")
                            input("Goblin: All you have to do is help me pick these grey stones. I need 10 more. \n*Shows you stone*")
                            reply = input("Goblin: So will you help me? \ny or n. ")
                            if(reply.lower() == 'y'):
                                input("Hmm, this seems to be the one")
                                input("*Coughing* What's going on?")
                                input("Goblin: Mwahahahaha, silly {}, you fell right for my trap..".format(myStats["Race"]))
                                input("Goblin: That's actually a paralasis stone you fool, and I'm the only one with the antedote...")
                                input("Goblin: Now give me all your money or I'll leave you here to die..")
                                reply = input("A)Give money \nB)Attempt to fight")
                                if(reply.lower() == 'a'):
                                    myStats["Gold"] = 0
                                    input("Ok here, take everything I have")
                                    input(" --- You gave all your gold ---")
                                else:
                                    input("You think this is enough to paralyse me!? If so then you are the true fool")
                                    input("Lets Fight!")
                                    winner = oneVsOneFight("Goblin",20,0)
                                    if(winner == "Goblin"):
                                        input("GAME OVER")
                                        reply = input("Do you want to load game? \n y or n... ")
                                        if(reply.lower() == "y"):
                                            name = str(myStats["name"])
                                            load(name)
                                            main()
                                            raise SystemExit
                                    else:
                                        input("*You jump on top of the lifeless goblin and maul him long after he has died*... ")
                                        input("*You fall unconcious*... ")
                                        input("--- You were found by a guard who returned you to a hospital ---")
                                        input("*You wake up next to a masked man*")
                                        reply = input("A)Did you save me? \nB)Who are you? \nC)......\n...")
                                        if(reply.lower() == 'a'):
                                            input("???: Yes, I found you passed out next to a dead goblin. When you recover you will heading straight to prison...")
                                            input("PRISON??! He poisoned me and then tried to take advantage of me, I was barely able to protect myself..")
                                            input("???: Tell that to the judge")
                                            input("Silverdangdogdiggitydelldave: Hey, I heard you were found passed out next to Mount Targon. I figured you had touched the parasalsis stone. I'm glad you got out okay. I probably should have given you this map to South MosesVille and told you about that  ...")
                                            input("--- Gained map to South MosesVille ---")
                                            input("Also don't worry about prison, I'll explain the situation to the mayor, I'm sure she'll understand")
                                            bag["SouthMosesVilleMap"] = mapToSouthMosesVille
                                        elif(reply.lower() == 'b'):
                                            input("???: I'm the gaurd who saved your life")
                                            input("Guard: But don't think you are going to be let out scot-free, I found a freshly killed goblin right next to you!")
                                            input("Silverdangdogdiggitydelldave: Hey, I heard you were found passed out next to Mount Targon. I figured you had touched the parasalsis stone. I'm glad you got out okay. I probably should have given you this map to South MosesVille and told you about that  ...")
                                            input("--- Gained map to South MosesVille ---")
                                            input("Also don't worry about prison, I'll explain the situation to the mayor, I'm sure she'll understand")
                                            bag["SouthMosesVilleMap"] = mapToSouthMosesVille
                                        else:
                                            input("Mayor: Hello {}, I have been asked by Silverdangdogdiggitydelldave the second to come visit you!..".format(myStats["name"]))
                                            input("Mayor: Normally I wouldn't fufill sucha request, but for my brother, it's hard to say no...")
                                            input("Mayor: He also asked me to give you a map to South MosesVille, so here it is...")
                                            input("--- Gained map to South MosesVille ---")
                                            input("Mayor: Gaurd! You can leave, your work here is done. Rest up sweet prince, you will need it for your adventure to South Mosesville...")
                                            input("Gaurd: Yes sir...")
                                            input("Thank you...")
                                            bag["SouthMosesVilleMap"] = mapToSouthMosesVille
                            else:
                                input("I would never waste so much time to help out a lower race pick up faeces colored stones.... ")
                                input("I came to fight so prepare yourself maggot!..")
                                input("Lets Fight!")
                                winner = oneVsOneFight("Goblin",20,0)
                                if(winner == "Goblin"):
                                    input("I-I-I-I LOST...")
                                    input("GAME OVER")
                                    reply = input("Do you want to load game? \n y or n... ")
                                    if(reply.lower() == "y"):
                                        name = str(myStats["name"])
                                        load(name)
                                        main()
                                        raise SystemExit
                                else:
                                    input("Goblin: Please spare my life, I'll do anything. I just wanted help to gather these stones")
                                    input("YOU ARE STILL TRYING TO TRICK ME INTO GATHERING THE PARALASIS STONES???!!")
                                    input("Goblin: H-h-how did you know what they were?..")
                                    input("*Stomps goblins head crushing his skull into pieces*")
                                    input("--- You now have a pure hatred towards all goblins ---")
                        elif(reply.lower() == 'b'):
                            input("Goblin: Oh come on man, give a brother a hand...")
                            input("A brother?? A lowly Goblin like yourself has no right to call me your brother...")
                            input("Now leave this mountain before I end you right here!..")
                            input("Goblin: You will regret your decision to oppose me!..")
                            input("I'll get you...")
                            winner = oneVsOneFight("Goblin",20,0)
                            if(winner == "Goblin"):
                                input("I-I-I-I LOST...")
                                input("GAME OVER")
                                reply = input("Do you want to load game? \n y or n... ")
                                if(reply.lower() == "y"):
                                    name = str(myStats["name"])
                                    load(name)
                                    main()
                                    raise SystemExit
                            else:
                                input("I'll let you live so you can tell all the other Goblins out there not to mess with me...")
                                input("I will restore my honor and someday become the firelord!..")
                                input("Goblin: Thank you {}, I shall remember you as the adventurer who spared the life of a goblin...".format(myStats["Class"]))
                                input("Remember the name {}...".format(myStats["name"]))
                        else:
                            input("Goblin: Hey, stay right there. Don't come any closer...")
                            input("Goblin: Stop, please...")
                            reply = input("What will you do? \nA)Continue walking forward \nB)Talk to him \nC)Charge at him recklessly \n... ")
                            if(reply.lower() == 'a'):
                                input("Goblin: If it's a fight you want it's a fight you're going to get...")
                                input("Don't mess with me!..")
                                winner = oneVsOneFight("Goblin",20,0)
                                if(winner == "Goblin"):
                                    input("I-I-I-I LOST...")
                                    input("GAME OVER")
                                    reply = input("Do you want to load game? \n y or n... ")
                                    if(reply.lower() == "y"):
                                        name = str(myStats["name"])
                                        load(name)
                                        main()
                                        raise SystemExit
                                else:
                                    input("I'll let you live so you can tell all the other Goblins out there not to mess with me...")
                                    input("I will restore my honor and someday become the firelord!..")
                                    input("Goblin: Thank you {}, I shall remember you as the adventurer who spared the life of a goblin...".format(myStats["Class"]))
                                    input("Remember the name {}...".format(myStats["name"]))
                            elif(reply.lower() == 'b'):
                                input("Unless someone makes the first move, nothing will happen...")
                                input("Goblin: Wh-what do you plan on doing?...")
                                input("In the end, there is no greater motivation than revenge")
                                input("*Walks closer*")
                                input("Goblin: Wh-what are talking about. Revenge??.")
                                input("In this world, there is only good and evil...")
                                input("that was the first universal truth I grasped from observing the world around me when I was a child.")
                                input("Every human being without exception ends up falling into one category or the other.")
                                input("Goblin: *Charges at you...*")
                                input("I'll get you...")
                                winner = oneVsOneFight("Goblin",20,0)
                                if(winner == "Goblin"):
                                    input("I-I-I-I LOST...")
                                    input("GAME OVER")
                                    reply = input("Do you want to load game? \n y or n... ")
                                    if(reply.lower() == "y"):
                                        name = str(myStats["name"])
                                        load(name)
                                        main()
                                        raise SystemExit
                                    else:
                                        raise SystemExit
                                else:
                                    input("Sakujo....")
                                    input("Sakujoo....")
                                    input("SAKUJOOOOOO....")
                                    input("*After being brutally attacked the goblin suffered a heart attack*")
                            else:
                                ("*You go to charge at goblin but he begins to charge at you*")
                                input("Come at me like your life depends on it!")
                                input("Get ready for the next battle")
                                winner = oneVsOneFight("Goblin",20,0)
                                if(winner == "Goblin"):
                                    input("I-I-I-I LOST...")
                                    input("DEFEAT!")
                                    reply = input("Continue? \n y or n... ")
                                    if(reply.lower() == "y"):
                                        name = str(myStats["name"])
                                        load(name)
                                        main()
                                        raise SystemExit
                                    else:
                                        raise SystemExit
                                else:
                                    input("Your strength mirrors a child's beguilement...")
                                    input("*Goblin takes final breath*")
                                    input("Weaklings should perish...")

        elif(reply.lower() == 'c'):
            input("What I do need is a map, I have no idea how to get to South MosesVille...")
            input("Silverdangdogdiggitydelldave: Hey wait up \n*grasping for air* I forgot to give you this...")
            input("--- Gained map to South MosesVille ---")
            input("Silverdangdogdiggitydelldave: It's a map.\nFollow this to get to South MosesVille. And what ever you do, don't touch any plants or climb any trees...")
            input("Silverdangdogdiggitydelldave: Im being serious. That forest is full of paralasis plants. I completely forgot to tell you about them earlier...")
            input("Silverdangdogdiggitydelldave: Safe travels {}.".format(myStats["Race"]))
            input("*Thank you world*")
        else:
            input("Invalid answer")
            testBattle()

    else:
        if(party[0] == "Silverdangdogdiggitydelldave"):
            if(d == "notStupid"):
                input("Hey Bob, what are you doing with that {}? ".format(myStats["Race"]))
                d = "lessStupid"
                print("\nEnter 'stats'/'options'/'s' or 'o' for your current stats")
            reply = input("A)Hey I thought your name was Silverdangdogdiggitydelldave?! \nB)*FacePalm* Really..'BOB' \nC)Do you know her? \n... ")
            if(reply.lower() == "a"):
                input("She just gets confused some times. \n*whispers* not in front of the kid...")
                input("You know I can hear you \nWhat have I gotten myself into...")
                party[0] = "Bob "
                input("Updated party list: {}".format(party[0]))
            elif(reply.lower() == "b"):
                input("That's BigBobbyCat to you!")
                input("Big, b-bobby, cat... ")
                input("Bbc \nWhat have I gotten myself into...")
                party[0] = "BigBobbyCat "
                input("Updated party list: {}".format(party[0]))
            elif(reply.lower() == "c"):
                input("Her.. how did you know his name?..")
                input("Rhind... \nWhat kind of game have you created...")
                input("who are you talking to {}?".format(myStats["name"]))
            elif(reply.lower() == "o" or reply.lower() == "s" or reply.lower() == "options" or reply.lower() == "stats"):
                options()
                testBattle()
            else:
                input("Invalid reply...")
                testBattle()
        input("{}: Okay so we should probably test your skills {}".format(party[0],myStats["name"]))
        input("Get ready for your first fight.")
        winner = oneVsOneFight(party[0],20,0)
        input("{} won the battle.".format(winner))
        if(winner == myStats["name"]):
            while(d == "notStupid" or d == "lessStupid"):
                input("{}: Nice skills. You're the real deal. Who taught you to fight?".format(party[0]))
                reply = input("A)My father\nB)My mother\nC)I taught myself\n... ")
                if(reply.lower() == "a"):
                    input("{}: Your father must be proud of you".format(party[0]))
                    reply = input("A)Yes indeed\nB)Actually quite the opposite\n... ")
                    if(reply.lower() == "a"):
                        input("{}: I think I would be too. You'll be a great adventurer".format(party[0]))
                    else:
                        input("{}: Oh, that's awful to hear...".format(party[0]))
                        input("It's the very reason I want to catch them all and become the best pokemon master...")
                        input("I mean, adventurer...")
                        input("{}: What's a pokemon master...".format(party[0]))
                        input("Don't worry")
                    break
                elif(reply.lower() == "b"):
                    input("{}: Your mother taught you how to fight, that's amazing...".format(party[0]))
                    input("Yes, she was the greatest {} in our whole village. But everything changed when the fire nation attacked".format(myStats["Race"]))
                    input("{}: OMG, that's awful what happened?..".format(party[0]))
                    input("I was just a kid, but ma had already taught me so much. But one day our village was raided by the fire nation murdering our strongest and taking many others as prisoners..")
                    input("It's the very reason I decided to become an adventurer.\n I want to seek revenge and kill the guy that killed my mom...")
                    input("{}: You're a true inspiration..".format(party[0]))
                    break
                elif(reply.lower() == "c"):
                    input("I've been training myself since a child. I used to get bullied a lot because my parents died when I was really young.")
                    input("I had no friends")
                    if(myStats["Class"] == "Rogue"):
                        input("But I won't run anymore.. I won't go back on my word.. Cause that's my ninja way")
                    else:
                        input("But I never gave up, I grinded hard to get where I am now.. Cause the grind never stops, 100% no breaks. We stay dream chasing")
                    input("{}: You're a true inspiration..".format(party[0]))
                    break
                else:
                    input("Invalid answer")
        else:
            input("{}: You were a formidable opponent. I look forward to our next battle.".format(party[0]))
            input("Yeah, ggwp {}...".format(party[0]))
            input("You know what? I challenge you to another battle right now?")
            input("{}: Right now?? Are you sure?".format(party[0]))
            input("As sure as I have ever been!!..")
            input("Lets duel...")
            input("My move...")
            winner = oneVsOneFight(party[0],20,0)
            input("{} won the battle.".format(winner))
            if(winner == party[0]):
                input("GAME OVER")
                reply = input("Do you want to load game? \n y or n... ")
                if(reply.lower() == "y"):
                    name = str(myStats["name"])
                    load(name)
                    main()
                    raise SystemExit
                else:
                    raise SystemExit
            else:
                input("I won, I did it! Now we're even 1-1")
                input("{}: You got lucky, it won't happen again.".format(party[0]))
                input("Do you want a final round to settle this?")
                input("{}: As much as I wanna curbstomp your bi*ch ass, I think I have had enough.".format(party[0]))
                input("So you are scared, I get it. I would be scared too if I had just been embarrased like you did just then..")
                input("{}: Cocky child you are.".format(party[0]))
    
    chapter = "3"
    ng = "stop"
    save(myStats["name"])

        

def oneVsOneFight(enemyName, enemyRange, canRun):
    enemyStats["name"] = enemyName
    myHealth = myStats["Constitution"]
    enemyHealth = enemyStats["Constitution"]
    myArmor = myStats["Armor"]
    enemyArmor = enemyStats["Armor"]
    turn = random.randint(1,2)
    winner = 1
    myStealthOn = 0
    enemyStealthOn = 0
    attackchoice = ""

    while(myHealth > 0 and enemyHealth > 0):
        attackCount = myStats["AttackCounter"]
        while(turn == 1):
            input("What would you like to do?")
            reply = input("A)Attack \nB)Use spell \nC)Use item \nD)Run \nE)Stealth \n...")
            if(reply.lower() == "a"):
                index = 1
                attackchoice = "x"
                for k in attack:
                    print("enter", index, " for", k)
                    index += 1
                print("Enter 'x' to go back")
                reply2 = input("Select attack: ")
                if(reply2 == ""):
                    print("Invalid attack")
                elif(reply2.lower() == "x"):
                    print("*Back*")
                elif(reply2.isalpha()):
                    print("Invalid attack")
                else:
                    index = 1
                    for x in attack:
                        attackchoice = x
                        testint = int(reply2)
                        if(index == testint):
                            break
                        index += 1

                    if(enemyStealthOn == 1):
                        input("Opponent was stealthed and you missed your attack")
                    else:
                        if(attackchoice == "stealth attack"):
                            if(myStealthOn == 0):
                                attackchoice = "unarmed"
                            
                        attackhit = random.randint(1,20)
                        if(attackhit >= enemyArmor):
                            enemyHealth -= attack[attackchoice]
                            if(enemyHealth < 0):
                                enemyHealth = 0
                            input("You hit your attack...")
                            input("Enemy health dropped to {}..".format(enemyHealth))
                        else:
                            input("Your attack missed...")
                    attackCount -= 1
                    if(myHealth <= 0 or enemyHealth <= 0):
                        break

            elif(reply.lower() == "b"):
                attackchoice = "x"
                index = 1
                for k in spellbook:
                    print("enter", index, " for", k)
                    index += 1
                print("Enter 'x' to go back")
                reply3 = input("Select spell: ")
                if(reply3 == ""):
                    print("Invalid attack")
                elif(reply3.lower() == "x"):
                    print("*Back*")
                elif(reply3.isalpha()):
                    print("Invalid attack")
                else:
                    index = 1
                    for x in spellbook:
                        attackchoice = x
                        if(index == reply3):
                            break
                        index += 1
                    attackhit = random.randint(1,20)
                    if(attackhit >= enemyArmor):
                        enemyHealth -= spellbook[attackchoice]
                        if(enemyHealth < 0):
                                enemyHealth = 0
                        input("Enemy health dropped to {}".format(enemyHealth))
                    else:
                        input("Your attack missed...")               
                    attackCount -= 1 

            elif(reply.lower() == "c"):
                input("No items available...")
       
            elif(reply.lower() == "d"):
                if(canRun == 0):
                    input("You cannot run in this situation...")

            elif(reply.lower() == "e"):
                stealthsuccess = random.randint(1,10)
                if(myStats["Stealth"] >= stealthsuccess):
                    myStealthOn = 1
                    input("You entered stealth...")
                attackCount -= 1
            
            elif(reply2.lower() == 'options'or reply2.lower() == 'stats' or reply2.lower() == 'o' or reply2.lower() == 's'):
                options()

            if(attackCount == 0):
                turn = 2       

        if(myHealth <= 0 or enemyHealth <= 0):
            if(myHealth < enemyHealth):
                winner = enemyName
            else:
                winner = myStats["name"]
            break

        while(turn == 2):
            opponentaction = 1 #random.randint(1,3)
            if(opponentaction == 1):
                if(myStealthOn == 1):
                    input("You dodged your opponents attack while in stealth")
                else:
                    attackhit = random.randint(1,20)
                    if(attackhit >= myArmor):
                        myHealth -= attack["short sword"]
                        if(myHealth < 0):
                            myHealth = 0
                        input("You were hit by your opponents attacked...")
                        input("Your health dropped to {}..".format(myHealth))
                    else:
                        input("enemy's attack missed...")
                turn = 1

        if(myHealth <= 0 or enemyHealth <= 0):
            if(myHealth < enemyHealth):
                winner = enemyName
            else:
                winner = myStats["name"]
            break
        
    return(winner)

def chapter3():
    print("To be continued")

def options():
    print("Stats:",myStats)
    print("Attacks and weapons:",attack)
    print("Resistances:",resistance)
    print("Inventory:",bag)
    print("Spells:",spellbook)
    print("Party:",party)
    input("Continue...")

main()