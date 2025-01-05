# oop.py

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed

    def fetch(self):
        return f"{self.name} is fetching the ball!"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Meow")
        self.color = color

    def scratch(self):
        return f"{self.name} is scratching the post!"


# Example usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Grey")

print(dog.speak())  # Output: Buddy says Woof
print(dog.fetch())  # Output: Buddy is fetching the ball!
print(cat.speak())  # Output: Whiskers says Meow
print(cat.scratch())  # Output: Whiskers is scratching the post!
