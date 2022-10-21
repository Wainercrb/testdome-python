'''
A user interface contains two types of user input controls: TextInput, which accepts all characters and NumericInput, which accepts only digits.

Implement the class TextInput that contains:

    > Method add(self, character) - adds the given character to the current value
    > Method get_value(self) - returns the current value

Implement the class NumericInput that:

Inherits TextInput

    > Overrides the add method so that each non-numeric character is ignored
    > For example, the following code should output "10":

input = NumericInput()
input.add("1")
input.add("a")
input.add("0")
print(input.get_value())

-------------------|-------------------
Difficulty: Easy
Duration: 15 min

Python 3.7.4, Base Test:

class TextInput:
    pass
  
class NumericInput:
    pass

if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())
'''

class TextInput:
    def __init__(self):
        self.value = ''

    def add (self, character):
        self.value += character

    def get_value(self):
        return self.value
  
class NumericInput(TextInput):
    def __init__(self):
      super().__init__()
    
    def add(self, value):
        if value.isnumeric():
            self.value += value

if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())