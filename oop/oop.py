class ptn:
    name=""
    hunger=0
    energy=0
    happiness=0
    tricks=[]
    def __init__(self,name,hunger,eneragy,hyppiness,tricks):
        self.name=name
        self.hunger=hunger
        self.energy=eneragy
        self.hyppiness=hyppiness
        self.tricks=tricks
    def eat(self):
        if self.hunger>0:   
            self.hunger-=3
            self.happiness+=1
        else:
            print(f"{self.name} are not hungry")
    def sleep(self):
        if self.energy>10:
            print(f"{self.name} are not sleepy")
        else:
            self.energy+=5
    def play(self):
        self.happiness+=2
        self.energy-=2
        self.hunger+=1
    
    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned {trick}!")
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")
    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
    
chu=ptn("cat",0,6,5,[]) #chu is my pet name
chu.eat()
chu.sleep()
chu.play()
chu.train("roll over")
chu.show_tricks()
chu.get_status()
