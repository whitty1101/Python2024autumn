class People:
    
    def __init__(self, eyeColor, hair):
        self.eyeColor=eyeColor
        self.hair=hair

    def introduce(self):
        print("My eyes are "+ self.eyeColor +" and my hair is "+ self.hair + ".")
    
    @classmethod
    def Am(cls):
        return cls("blue", "brown")

    @classmethod
    def Tai(cls):
        return cls("black", "black")

Taiwanese=People.Tai()
Taiwanese.introduce()
American=People.Am()
American.introduce()
