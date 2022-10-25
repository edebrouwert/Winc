# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality
    }
    return passport
print(create_passport("erwin", "30 aug", "diessen", "185cm", "NL"))


def add_stamp(passport, country):
    if country not in passport.values():
        if "stamps" not in passport:
            passport.update({"stamps": [country]})
        else: 
            passport["stamps"].append(country)
    return passport

print(add_stamp(create_passport("erwin", "30 aug", "diessen", "185cm", "NL"), "NL"))

def add_biometric_data(passport, typebiometricdata, values, date):
    if "biometric" not in passport.keys():
        passport["biometric"] = {}
#    if typebiometricdata not in passport["biometric"].keys():
    passport["biometric"].update({typebiometricdata: {
        "date": date,
        "value": values
        }})
    return passport

omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_left", "brown", "2022-01-10")
fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}
omari = add_biometric_data(omari, "finger_prints", fingerprint_data, "2022-01-12")
print(omari)
