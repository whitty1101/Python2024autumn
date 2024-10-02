class Person:
    #contructor
    def __init__(self, name, age, favoriteFood):
        self.name=name
        self.age=age
        self.favoriteFood=favoriteFood

    def introduce(self):
        print("I'm"+ self.name +"and I am "+ str(self.age) + " years old. I like to eat "+ self.favoriteFood +".")
        
    def shout(self, content):
        print("I shouted, " +content +".")

amy=Person("Amy", 15, "Apple")
amy.introduce()
amy.shout("I hate dentist")