# LAB 10
# Ruvi Jaimes

# Defines the class Car with attributes color, model, 
# number of doors, owner name, and max speed. 

class Car(object):
    count = 0
    def __init__(self, color, model,no_of_doors, owner, max_speed):
        self.color = color
        self.model = model
        self.no_of_doors = no_of_doors
        self.owner = owner
        self.max_speed = max_speed
        Car.count += 1
        
        
        
    def __str__(self):
        return "Car model {} has color {}, {} doors, max speed {} and is owned by {}."\
                     .format(self.model, self.color, self.no_of_doors, self.max_speed, self.owner)
    
    def __del__(self):
        Car.count -= 1
    def set_color(self, new_color):
        self.color = new_color
        
    def set_max_speed(self, new_max_speed):
        self.max_speed += new_max_speed
        
def main():
    car1 = Car("red","Ford",4,"Ruvi",250)
    print(car1)
    car1.set_max_speed(-50)
    print(car1)
    print("You have these many cars: ", Car.count)
    car2 = Car("pink", "Volkswagon",4,"Esmeralda", 320)
    car3 = Car("navy", "Jeep", 2, "Yesai", 300)
    print("You have these many cars: ", Car.count)
    del car1
    print("You have these many cars: ", Car.count)
    
main()
