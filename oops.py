# class MyClass:
#     variable = 'blah'
    
#     def function(self):
#         print('This is a message inside the class')


# myobjectx = MyClass()

# print(myobjectx.variable)

# myobjectx.function()

# class NumberHolder:
#     def __init__(self,number):
#         self.number = number

#     def returnNumber(self):
#         return self.number

# var = NumberHolder(7)
# print(var.returnNumber())       


# class Dog:
#     def __init__(self,name,breed):
#         self.name = name;
#         self.breed = breed;

#     def bark(self):
#         print(f"{self.name} says woof")



# dog1 = Dog('enzo','lab')
# dog2 = Dog('ferrari','rott')


# dog1.bark()


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle()
car1.name='fer'
car1.color='red'
car1.kind='convertible'
car1.value=60000

car2 =Vehicle()
car2.name='jump'
car2.kind='van'
car2.color='blue'
car2.value=1000000

# test code
print(car1.description())
print(car2.description())