# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(x):
    return f"Hello, {x}"

print(greet("Erwin"))

def add(a, b, c):
    return a + b + c

print(add(1,2,3))

def positive(x):
    if x > 0:
        return True
    else: return False

print(positive(0))

def negative(x):
    if x < 0:
        return True
    else: return False

print(negative(0))