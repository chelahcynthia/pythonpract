# Python constructor
class Car:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    
    def start(self):
        self.started = True
        print("Car started, let's ride!")
        
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("vrooooom!")
        else:
            print("You need to start the car first")
            
    def  stop(self):
        self.speed = 0