
# Basic Function
def greet():
    print("Hello")

greet()

# Function with Parameter
def greet(name):
    print(f"Hello, {name}!")

greet("sowju")

# Function with multiple Parameters
def sum(a,b):
    return a + b

print(f"Hello, the sum of 2,3 is {sum(2,3)}")

# Default parameters
#Functions can have default values for parameters. If an argument is not provided, the default value is used
def greet_def(name="San Francisco"):
    print(f"Hello {name}")

greet_def("Sowju")
greet_def()

# Keyword Arguments
# You can call functions with keyword arguments, where you specify the parameter names
def describe_town(name,state):
    print(f"City {name} is in the state of {state}")

describe_town(name="San Francisco",state="California")
describe_town(name="Austin",state="Texas")

# Arbitrary number of Arguments *args
def print_fruits(*names):
    for name in names:
        print(f"This is a {name}")

print_fruits("Apple", "Mango", "Banana")

# Aribitrary number of Keyword Arguments **kwargs
def print_kv(**city_state):
    for k,v in city_state.items():
        print(f"Key is {k} Value is {v}")
    
print_kv(city="Sacramento",state="California")