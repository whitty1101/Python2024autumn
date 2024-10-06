#==封裝encapsulation=========================================================================
'''
class Person:
    @staticmethod
    def work(working_hour):
        print("working hour: ", working_hour)
amy=Person()
amy.work(8)

class Student:
    def __init__(self, name):
        self.__name=name
        self.__score={"Math": 0, "Physics": 0, "Chemistry": 0}
    #私有方法
    def __add_subject(self, subject):
        self.__score[subject]=0
    #工友方法
    def set_score(self, subject, score):
        if subject not in self.__score:
            self.__add_subject(subject)
        self.__score[subject]=score

    def get_subject(self):
        for key in self.__score:
            print(key, self.__score[key])

peter=Student("peter")
peter.set_score("math",100)
peter.get_subject()
'''
#==封裝encapsulation=========================================================================


#==繼承Inheritance===========================================================================
#被繼承的類別 ->父類別
class Person: #1
    def __init__(self, name, age, ID):
        self.name=name
        self.age=age
        self.__ID = ID
    def speak(self, sentence):
        return self.name+"says" +sentence
#繼承PERSON的類別-> 子類別
class Athlete(Person):
    def workout(self):
        return '%s goes to the gym to exercise.' %(self.name)
    #複寫建構子
    def __init__(self, name, age, ID, height):
        super().__init__(name, age, ID) # 1
        self.height=height
    #複寫SPEAK方法
    def speak(self, sentence):
        print('Athelete: ', super().speak(sentence)) # 2
#==繼承Inheritance===========================================================================
#Polymoehism
import abc

class Member(metaclass=abc.ABCMeta):
    def __init__(self, name, level):
        self.name=name
        self.level=level

    @abc.abstractmethod
    def discount(self,price):
        pass

    def buy(self, price):
        d_price=self.discount(price)
        print(self.name, "'s member level is ", self.level, ". After discount: ", d_price)
class GoldenMember(Member):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.discount_rate=0.9
    def discount(self, price):
        return price*self.discount_rate

class VIPMember(Member):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.discount_rate=0.8
    def discount(self, price):
        return price*self.discount_rate
john= GoldenMember('John','Golden')
amy=VIPMember("amy","Golden")
john.buy(2000)
amy.buy(2000)