class Animal:
    def __init__(self, name):    
        self.name = name
        self.limbs=4
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")
    def limbs(self):
        return self.limbs
    

class Cat(Animal):
    '''inherets from animal class'''
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    '''polymorphis on the use of talk funtion'''
    def talk(self): 
        return 'Woof! Woof!'


pet=Cat('pussy');
print pet.limbs '''abstraction by using the object '''
