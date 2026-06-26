# INHERITANCE

class Animal: 
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        print(f"{self.name} says {self.sound}")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "meow")
        self.indoor = True

    def purr(self):
        print(f"{self.name} purrs...🐱")

cat = Cat("Whiskers")
cat.speak()
cat.purr()
