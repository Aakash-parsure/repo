class Bird:
    def intro(self):
        print("There are many types of birds.")
    
    def flight(self):
        print("Most of the birds can fly but some can't.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly.")


obj_brd = Bird()
obj_sprw = Sparrow()
obj_ost = Ostrich()

obj_brd.intro()
obj_brd.flight()

obj_sprw.intro()
obj_sprw.flight()

obj_ost.intro()
obj_ost.flight()







