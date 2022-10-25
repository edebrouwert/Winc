from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.

def unique_koala_facts(number):
    uniquelist = []
    if number > 1000:
        number = 1000
    count = 0
    while (len(uniquelist) < number) and count < 1000:
        count = count + 1
        singlefact = random_koala_fact()
        if singlefact not in uniquelist:
            uniquelist.append(singlefact)
    return uniquelist


def num_joey_facts():
    joeycounter = 0
    usedfactlist = []
    joeyfacts = []
    while usedfactlist.count(random_koala_fact()) < 11:
        singlefact = random_koala_fact()
        usedfactlist.append(singlefact)
        if "joey" in singlefact and (singlefact not in joeyfacts):
            joeycounter = joeycounter + 1
            joeyfacts.append(singlefact)
    print(joeycounter)
    return joeycounter


num_joey_facts()


def koala_weight():

    for i in unique_koala_facts(1000):
        if "kg" in i:
            print(i[-5:-3])
            return int(i[-5:-3])


koala_weight()
