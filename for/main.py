from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
#1 Exercise 1
def shortest_names(countrylist):
    shortest_countrylist = [countrylist[0]]
    for i in countries:
        if len(i) < len(shortest_countrylist[0]): 
            shortest_countrylist = [i] #if length of current item is smaller than what is in the list, empty list and then add current item
        elif len(i) == len(shortest_countrylist[0]):
            shortest_countrylist = shortest_countrylist + [i]
    print(shortest_countrylist)
    return shortest_countrylist

#Exercise 2
vowel_list = ["a", "e", "i", "o", "u"]

def vowelcounter(word):
    count = 0
    for letter in word:
        if letter.lower() in vowel_list:
            count = count + 1
    return count

def most_vowels(countrylist):
    sorted_country_vowel_list = [countries[0]]
    for country in countrylist:
        if vowelcounter(country) > vowelcounter(sorted_country_vowel_list[0]):
            sorted_country_vowel_list = [country] + sorted_country_vowel_list
        else: 
            sorted_country_vowel_list = sorted_country_vowel_list + [country]
    print(sorted_country_vowel_list[:3])
    return sorted_country_vowel_list[:3]

def alphabet_set(countries):
    used_letters = []
    used_country_list = []
    distinctcountrylist = set(countries)
    for country in distinctcountrylist: #loop over countries
        addedletters = False
        for i in distinct_letters(country): #loop over the distinct letters in a country
            if i.lower() in used_letters or (len(distinct_letters(country)) <8): #if a letter is used or number of distinct letters <8, do nothing
                continue
            else: #if a letter is not yet used, add it to the used letters list
                used_letters = used_letters + [i.lower()]
                addedletters = True
        if addedletters == True: #if at least one of the country's letters is used, add it to the used country list
            used_country_list = used_country_list + [country]
        if len(used_letters) >= 26: #if number of used letters is 26, it means the whole alphabet is used
            break
        else: 
            continue
    print(used_country_list)
    return used_country_list


#Exercise 3
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def distinct_letters(word):
    letterlist = []
    for letter in word:
        if letter in alphabet:
            letterlist = letterlist + [letter]
    distinctletterlist = set(letterlist)
    return distinctletterlist




# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """




shortest_names(countries)
most_vowels(countries)
alphabet_set(countries)

