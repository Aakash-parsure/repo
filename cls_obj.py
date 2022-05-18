class Dog:
    attr1="mammal"

    def __init__(self,name):
        self.name=name

    def speak(self):
        print("{} speaks".format(self.name))


Roger = Dog("Roger")
Tommy = Dog("Tommy")

print("My name is {}".format(Roger.name))
print("My name is {}".format(Tommy.name))

print("Roger is a {}".format(Roger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

Roger.speak()
Tommy.speak()
