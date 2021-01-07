class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print("Animal's sound")
        return self.name, self.age

class Cat(Animal):
    def __init__(self, name, age, sound):
        super(Cat, self).__init__(name, age, sound)

    def make_sound(self):
        return self.sound

class Dog(Animal):
    def __init__(self, name, age, sound):
        super(Dog, self).__init__(name, age, sound)

    def make_sound(self):
        return self.sound


c = Cat('gerkules', 2, 'meow')
d = Dog('alishs', 4, 'gav')
print(c.make_sound())
print(d.make_sound())
