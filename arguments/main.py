# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Exercise 1
def greet(name, template = "Hello, <name>!"):
    greeting = template.replace("<name>", name)
    return greeting


#Exercise 2
def force(mass, body= "earth"):
    gravitydict = {"sun": 274, "jupiter": 24.9, "neptune": 11.2, "saturn": 10.4, "earth": 9.8, "uranus": 8.9, "venus": 8.9, "mars": 3.7, "mercury": 3.7, "moon": 1.6, "pluto": 0.6}
    body.lower()
    new_dict = {k: float(v) for k, v in gravitydict.items()}
    force = float(mass) * new_dict[body]
    return force


#Exercise 3
def pull(m1, m2, d):
    pull = (6.674 * (10**-11)) * (((float(m1) * float(m2))/(float(d)**2)))
    return pull

