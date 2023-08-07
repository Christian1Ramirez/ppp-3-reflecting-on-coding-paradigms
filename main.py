# Functional Prompt
# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_sort(nested_list):
    return sorted([j for i in nested_list for j in i])

test_arr = [[3, 5], [7, 3, 9], [1, 12]]

res = flatten_sort(test_arr)

print(res)



"""
How does this solution ensure data immutability?
    The solution does not modify the input nested_list. 
    Instead, it creates a new list using a list comprehension and then sorts that list, returning the sorted version. 

Is this solution a pure function? Why or why not?
    Yes, this solution is a pure function. 
    A pure function is a function where the output value is determined only by its input values, without observable side effects.

Is this solution a higher order function? Why or why not?

    No, this solution is not a higher-order function. A higher-order function is a function that takes one or more functions as arguments, 
    and/or returns a function as its result. 
    The flatten_sort function does not accept any 
    function as an argument nor does it return a function.

Would it have been easier to solve this problem using a different programming style?
    Perhaps, but would defeat the purpose of the excercise.

Why in particular is functional programming a helpful paradigm when solving this problem?
    Its easier to prevent unintended side-effects since the OG data structure does not change. Its also
    self contained and does not rely on external state or data making it more predicable and readable
"""


# Watto needs a new system for organizing his inventory of podracers. Help him do this by 
# implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

# Define a repair() method that will update the condition of the podracer to "repaired".

    def repair(self):
        self.condition = "repaired"

# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

# Define another class that inherits Podracer and call this one SebulbasPod. 

class SebulbasPod(Podracer):

# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

    def flame_jet(self):
        self.condition = "trashed"

# Testing the changes
# Test 1
pod = Podracer(400, "trashed", 800)
pod.repair()
print(pod.condition)  

# Test 2
new_pod = AnakinsPod(2, "perfect", 1000)
new_pod.boost()
print(new_pod.max_speed) 

# Test 3
third_pod = SebulbasPod(600, "repaired", 1200)
third_pod.flame_jet()
print(third_pod.condition) 

    


