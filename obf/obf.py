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
        "penetration": "got speared lmao kekw",
        "eye penetration": "One of your party members had been hit in the eye.",
        "group": "Some group of robbers robbed your party. Some valuables had been lost, but some were well-hidden.",
        "stockings": "Your party had a few pairs of stockings, got as a charity donation.",
        "nakadashi": "You shot an arrow right at the bullseye of the target.",
        "schoolgirl uniform": "Some schoolgirl joined your party.",
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
        "big nipples": "You had somehow met (got caught) the captain of Houshou pirates.",
        "big penis": "\"Carrying a meat obelisk isn't a bad idea\", they said.",
        "big vagina": "A human sinkhole. Figuratively.",
        "bike shorts": "You had met a person riding a bike in bike shorts.",
        "bikini": "Your party went to the beach to admire the view (really just the womans over there).",
        "birth": "You went to help a woman deliver a baby because the hospital is too far away.",
        "bisexual": "Double dealing character.",
        "blackmail": "dude, i know you really wanted that crystal, but blackmailing? really?",
        "blind": "Your party helped a blind person cross the road. <3",
        "blindfold": "Putting a blindfold on an idiot of a robber that tried to rob you.",
        "blood": "Your party fought a ferocious battle that spilled blood everywhere.",
        "bloomers": "You photographed some people in their bloomers. Creep.",
        "blowjob": "Your party went to get some ice-cream.",
        "blowjob face": "Your party decided to take some photos while eating ice-cream.",
        "body modification": "<100 percent human.",
        "body painting": "Have you saw the video that one women was walking through NYC with no pants and just painting?",
        "bodystocking": "You met someone wearing a ridiculously big size stockings.",
        "bodysuit": "You saw someone riding a bike with a full bodysuit on. Wonder where they're going.",
        "body swap": "Some of your party members suddenly switched bodies with each other while fighting a witch.",
        "body writing": "A human body isn't a public bathroom stall. Or maybe it is, I don't know.",
        "bondage": "You got robbed by a group of robbers and they tied you onto the trees. Though with enough tries, the trees came off because they weren't very big.",
        "bowbows": "You met a person named bowbows.",
        "braces": "You met a person named braces, who is also wearing braces.",
        "brain fuck": "++++++[>++++++++++<-]>++++<++[>+++++++<-]>.[>+<]>+.",
        "breast expansion": "You got a big, juicy chicken breast, and now it's even bigger.",
        "breast feeding": "goo goo gaa gaa, here's your milk since you wanted to act like a fucking baby",
        "bride": "A member of your party is just married.",
        "brother": "One of your party member also had their brother join your party as well.",
        "bukkake": "Get caked, lmao",
        "bull": "You rode a bull, for funs and gigs.",
        "bunny girl": "You met a bunny that can transfrom itself into a girl.",
        "bunny boy": "You met a guy wearing a bunny suit.",
        "buranran": "You met a guy named Buranran.",
        "burping": "You had quite a fun party drinking liquors and let out a burp of enjoyment.",
        "business suit": "One of your party members used to be an office worker.",
        "butler": "You met visited a local lord's mansion and the butler was very handsome.",
        "cannibalism": "You encountered a cannibalistic tribe and decided to go back the other way as fast as possible.",
        "cashier": "You encountered a beautiful cashier at the local shop.",
        "catboy": "You met a boy of the Neko tribe.",
        "catfight": "You witnessed a fight between some people of the Neko tribe.",
        "catgirl": "You met a girl of the Neko tribe.",
        "cbt": "Cock and ball torture (CBT), penis torture or dick torture is a sexual activity involving application of pain or constric--",
        "centaur": "You met a centaur. He was a very nice guy.",
        "cephon": "You met a guy named Cephon.",
        "cervix penetration": "One of your female party members got speared, vertically, and destroyed their insides. Ouch.",
        "chastity belt": "Frequent mana outburst led to one of your member being put on a magic limiter.",

    }

    for tag in tags:
        tags[tags.index(tag)] = dict.get(subtags, tag, tag)
    return "\n\\".join(tags)
