from collections import defaultdict

def obfuscate(d):
    """TODO: Take the tags, and swab the tags with an adventurous version of the tags.
    I'm really lazy and if you have spare time, add to this function and submit a pull request."""

    tags = list(d.tags)
    subtags = {
        "sole male": "Your party had a single male, how lame.",
        "sole female": "Your party hds a single female, how lame.",
        "threesome": "A three person party, sounds like a fun party to me.",
        "wholsesome": "Your party had a great time.",
        "ugly bastard": "Your party encountered... quite a heinous beast... ew.",
        "tentacles": "Your party got caught by a squid-octupus-thing, fortunately it was easy to get out of.",
        "cervix penetration": "One of your female party members got speared, vertically, and destroyed their insides. Ouch.",
        "penetration": "got speared lmao kekw",
        "eye penetration": "One of your party members had been hit in the eye.",
        "group": "Some group of robbers robbed your party. Some valuables had been lost, but some were well-hidden.",
        "stockings": "Your party had a few pairs of stockings, got as a charity donation.",
        "nakadashi": "You shot an arrow right at the bullseye of the target.",
        "schoolgirl uniform": "Some schoolgirl joined your party.",
        "blowjob": "Your party went to get some ice-cream.",
        "double penetration": "got speared, twice kekw",
        "story arc": "Your party decided to take a break from continuing forward and just wrote down all the stories they had been up against.",
        "incest": "Two of your party members have found themselves in love with each other.",
        "x-ray": "You acquired mana vision",
        "0109samurai": "You met a guy named 0109samurai.",
        "35 machi": "You met a guy named 35 machi.",
        "3d": "You somehow was able to gain control over an extra spacial dimension.",
        "abortion": "Heavy damage to one of your female party members caused a miscarriage.",
        "act-fancer": "Tasted a retro game.",
        "adventitious mouth": "One of your party member grew a mouth in the wrong place after dealing with toxic wastes.",
        "adventitious penis": "One of your party member grew a schlong in the wrong place after dealing with toxic wastes.",
        "adventitious vagina": "One of your party member grew a *cat* in the wrong place after dealing with toxic wastes.",
        "afro": "You grew an afro hair.",
        "age progression": "Your party grew old.",
        "age regression": "Your party grew young.   Wait what the fuck?",
        "ahegao": "One of your party members is good at making funny facial expressions and should have been a comedian.",
        "aji ponntarou": "You met a guy named Aji Ponntarou.",
        "akai toreno": "You met a guy named Akai Toreno.",
        "akaozaka": "You met a guy named Akaozaka.",
        "akigami satoru": "You met a guy named Akigami Satoru.",
        "akira roji": "You met a guy named Akira Roji.",
        "a kyokufuri": "You met a guy named A Kyokufuri.",
        "alien": "You met an extraterrestrial being.",
        "alien girl": "You met an extraterrestrial female being.",
        "all the way through": "One of your party member is speared like a skewer.",
        "almirua": "You met a guy named almirua",
        "already uploaded": "Plagiarism bad",
        "amputee": "You met an amputated person just chilling outside.",
        "ana kichi": "You met a guy named Ana Kichi.",
        "anal": "Watch where you take a dump, snakes are relentless.",
        "anal birth": "Giving birth... through the anus. How the fuck",
        "analphagia": "Unable to swallow... through the anus. What the fuck",
        "angel": "You, quite figuratively, met an angel.",
        "animated": "How the hell did you put a video recording in a book??",
        "animegao": "You met an Animegao Kigurumi.",
        "anorexic": "One of your party member suffered from anorexia, that is the loss of the ability to eat or be hungry.",
        "anthology": "Your party members wanted to add their own entries to the story journal.",
        "aoi frasco": "You met a guy named Aoi Frasco",
        "aoki rinko": "You met a guy named Aoki Rinko",
        "a.pg": "You met a guy named a.pg.",
        "apparel bukkake": "Your favorite clothes was dirtied.",
        "apron": "One of your party members cooked some food in an apron",
        "aps": "You met a guy named aps.",
        "aps matsumoto": "You met a guy named aps matsumoto.",
        "arata rokka": "You met a guy named arata rokka.",
        "ari and mura": "You met some guys named Ari and Mura.",
        "arice": "You met a guy named Arice.",
        "armpit licking": "wakipai peropero yes",
        "armpit sex": "wakipai tsuyotsuyo yes",
        "artbook": "An artbook made for you.",
        "artistcg": "You met a guy that does CGs.",
        "ashita wo sakigakeru kyouki shuudan": "You had encountered a tome with the title 'Ashita wo Sakigakeru Kyouki Shuudan'.",
        "asphyxiation": "One of your party members was nearly choked to death.",
        "ass expansion": "w i d e a s s",
        "assjob": "shirikoki",
        "atotama": "You met a guy named Atotama.",
        "aunt": "Your aunt came to visit.",
        "autofellatio": "Everyone needs some self-comfort once in a while, and so does you.",
        "autopaizuri": "One of your party member needs some self-comforting after some of those traumas",
        "ayako hanabishi": "You met a guy named Ayako Hanabishi.",
        "ayakouji haruna": "You met a guy named Ayakouji Haruna.",
        "azisaikyou": "You met a guy named Azisaikyou.",
        "az project": "You met a guy named AZ Project.",
        "azumari": "You met a guy named Azumari.",
        "baa": "You met a guy named Baa.",
        "bald": "You had encountered a bald guy",
        "balljob": "One of your party member found and played with a ball they had found.",
        "ball expansion": "Ball gets filled with... something.",
        "bandages": "Bruise healer, yeah.",
        "bankoku ayuya": "You met a person named Bankoku Ayuya.",
        "bat girl": "You met a girl who is apparently a bat.",
        "bbm": "You met a big black man. He is not particularly aggresive though.",
        "bbw": "You met a big black women. Just trying to make a living out here.",
        "bdsm": "You met a master and a slave. They are working very gratiously.",
        "bear": "You had encountered a bear.",
        "bear girl": "You had encountered a female bear.",
        "beauty mark": "You had encountered a person with a beauty mark. \"Truly is a beauty\", you said.",
        "bee girl": "You had met a queen bee that can turn into a human at will.",
        "bestiality": "You know, messing with that animal over there could have been a very bad idea.",
        "big areolae": "You had encountered a big flower field.",
        "big ass": "You had had some delicious, juicy 2%)6#^@ ass.",
        "big balls": "Your party had found a big bouncy ball.",
        "big breast": "You had had some delicious chicken breasts.",
        "big clit": "\"Carrying a goddamn obelisk isn't a bad idea\", they said.",
        "big lips": "You had visited a theatre with oversized curtains.",
        "big muscles": "You had met a very buffed guy. He challenged your team, but you refused.",
        "big nipples": "You've somehow met (got caught) the captain of Houshou pirates.",
        "big penis": "\"Carrying a meat obelisk isn't a bad idea\", they said."
    }

    for tag in tags:
        tags[tags.index(tag)] = dict.get(subtags, tag, tag)
    return "\n".join(tags)
