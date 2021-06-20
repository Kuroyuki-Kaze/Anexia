from NHentai.entities.doujin import Doujin
from NHentai.nhentai import NHentai
from obf import obf

Nhentai = NHentai()

def printDoujin(dj):
    r = []
    m = []
    if dj != None:
        m.append("**Adventure Title:** " + str(dj.title))
        m.append("**Also known as (might not display properly):** " + str(dj.secondary_title))
        m.append("**Guide(s):** " + str(dj.artists))
        m.append("**List of things you've done:** " + "\n" + str(dj.tags))
        m.append("**Journey's written language(s):** " + str(dj.languages))
        m.append("**Journey book's classification:** " + str(dj.categories))
        m.append("**Guild:** " + str(dj.groups))
        m.append("**Party members:** " + str(dj.characters))
        m.append("**Adventure parody:** " + str(dj.parodies))
        m.append("**The number of pages of the book:** " + str(dj.total_pages))
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

def printSearchDoujin(query: str, sort: str, page: str) -> list:
    search_obj = Nhentai.search(query=query, sort=sort, page=page)
    r = []
    r.append("**Query was:** " + str(search_obj.query))
    r.append("**Sort was:** " + str(search_obj.sort))
    r.append("**Total results:** " + str(search_obj.total_results))
    r.append("**Total result pages:** " + str(search_obj.total_pages))
    r.append("**Doujins:** ")
    
    for doujin in search_obj.doujins:
        r.append(f"ID: {doujin.id}\nTitle: {doujin.title}\nLanguage: {doujin.lang}")
    
    return r

def printdoujin(derID, obffact):
    try:
        doujin: Doujin = Nhentai.get_doujin(id=int(derID))
        if obffact == "-o":
            doujin.tags = obf.obfuscate(doujin)
        else:
            doujin.tags = "\n".join(doujin.tags)
        final = printDoujin(doujin)
        return final
    except ValueError:
        if derID == "random":
            rdoujin: dict = Nhentai.get_random()
            final = printrDoujin(rdoujin)
            return final
        else:
            return "Bad input."