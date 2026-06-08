class Robot:
    def __init__(self, name, model, primary_function, power_level):
        self.name = name  
        self.model = model 
        self.function = primary_function 
        self.power = power_level

    
    def introduce(self):
    
        print(f" [SYSTEM UPDATE] Initializing introduction protocols...")
        print(f"Hello, human! My name is {self.name}.")
        print(f"I am a model {self.model} unit.")
        print(f"My primary directive is: '{self.function}'.")
        print(f"Current battery level: {self.power}%")
        print("-" * 45)

    def perform_task(self):
       
        if self.power > 10:
            print(f"{self.name} is now executing: {self.function}.")
            self.power -= 10 
            print(f"Remaining battery: {self.power}%")
        else:
            print(f"Warning! {self.name} has low power. Please recharge.")
        print("-" * 45)



robot1 = Robot("Sparky", "X-200", "Assisting humans with coding", 100)
robot2 = Robot("IronClad", "Heavy-Duty v4", "Lifting heavy boxes in warehouses", 15)




robot1.introduce()
robot1.perform_task()

robot2.introduce()
robot2.perform_task()