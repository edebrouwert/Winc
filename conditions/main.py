
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_day, cow_milking_status, location, season, slurry_tank, grass_status):
    if location == "pasture" and (time_of_day == "night" or weather == "rainy"):
        return "take cows to cowshed"
    elif cow_milking_status == True:
        if location == "cowshed":
            return "milk cows"
        elif location == "pasture":
            return """take cows to cowshed\nmilk cows\ntake cows back to pasture"""
    elif slurry_tank == True and (weather != "sunny" and weather != "windy"):
        if location == "cowshed":
            return "fertilize pasture"
        elif location == "pasture":
            return "take cows to cowshed \n fertilize pasture \n take cows back to pasture"
    elif grass_status == True and season == "spring" and weather == "sunny":
        if location == "pasture": 
            return "take cows to cowshed \n mow grass \n take cows back to cowshed"
        return "mow grass"
    else:
        return "wait"

farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)                       