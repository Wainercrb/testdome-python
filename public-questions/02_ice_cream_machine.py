'''
Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping. If there are no ingredients or toppings, the method should return an empty list.

For example, IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops() should return [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].

---------------|----------------
Difficulty: Easy
Duration: 10 minTime:


Python 3.7.4, Base Test:
class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        pass

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
'''

class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        result, ingredient_position, toppin_position = [], 0, 0

        if (len(self.ingredients) <= 0 or len(self.toppings) <= 0):
            return result

        for _ in range(len(self.ingredients) * len(self.toppings)):
            result.append([self.ingredients[ingredient_position], \
                           self.toppings[toppin_position]])
            
            ingredient_position += 1
            if len(self.ingredients) <= ingredient_position:
                ingredient_position = 0
                toppin_position += 1
        
        return result

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate", 'vanilla2112'], ["chocolate sauce", 'vanilla'])
    print(machine.scoops()) #should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]