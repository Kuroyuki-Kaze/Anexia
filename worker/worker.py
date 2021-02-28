import nhentai
Nhentai = nhentai.NHentai()

def printDoujin(dj):
    r = []
    m = []
    if dj != None:
        m.append("Adventure Title: " + str(dj.title))
        m.append("Also known as (might not display properly): " + str(dj.secondary_title))
        m.append("Guide(s): " + str(dj.artists))
        m.append("List of things you've done: " + str(dj.tags))
        m.append("Journey's written language(s): " + str(dj.languages))
        m.append("Journey book's classification: " + str(dj.categories))
        m.append("Guild: " + str(dj.groups))
        m.append("Party members: " + str(dj.characters))
        m.append("Adventure parody: " + str(dj.parodies))
        m.append("The number of pages of the book: " + str(dj.total_pages))
        n = "\n".join(m)
        r.append(n)
        r.append(str(dj.images[0]))
        return r
    else:
        return "You went adventuring and you found... absolutely nothing. Try again with a better seed, nub."

def printrDoujin(dj):
    r = []
    m = []
    m.append("Seed number: " + str(dj.id))
    m.append("Adventure Title: " + str(dj.title))
    m.append("Also known as (might not display properly): " + str(dj.secondary_title))
    m.append("Guide(s): " + str(dj.artists))
    m.append("List of things you've done: " + str(dj.tags))
    m.append("Journey's written language(s): " + str(dj.languages))
    m.append("Journey book's classification: " + str(dj.categories))
    m.append("Guild: " + str(dj.groups))
    m.append("Party members: " + str(dj.characters))
    m.append("Adventure parody: " + str(dj.parodies))
    m.append("The number of pages of the book: " + str(dj.total_pages))
    n = "\n".join(m)
    r.append(n)
    r.append(str(dj.images[0]))
    return r

def printdoujin(derID):
    try:
        doujin: dict = Nhentai._get_doujin(id=int(derID))
        final = printDoujin(doujin)
        return final
    except ValueError:
        if derID == "random":
            rdoujin: dict = Nhentai.get_random()
            final = printrDoujin(rdoujin)
            return final
        else:
            return "Bad input."