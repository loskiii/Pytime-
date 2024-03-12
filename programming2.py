class Dog:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
        
    def Call_dog(self):
        print("Hey", self.Name)    
        
Dog1 = Dog("snoopy", 5)
Dog1.Call_dog()
        