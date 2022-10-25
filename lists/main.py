# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line



toto_album_list = ["Fahrenheit", "The Seventh One", "Toto XX", "Falling in Between", "Toto XIV", "Old Is New"]
def remove_toto_albums(film_list):
    for i in film_list:
        if (i in toto_album_list):
            film_list.remove(i)
    print(film_list)
    return film_list

remove_toto_albums(["Toto XX", "hoi", "Toto XIV", "Fahrenheit"])


