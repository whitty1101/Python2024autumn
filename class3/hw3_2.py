from abc import ABC, abstractmethod


class Sport(ABC):
    @abstractmethod
    def play(self):
        pass
class Basketball(Sport):
    def play(self):
        return "playng basketball takes 2 hr"
    

class Baseball(Sport):
    def play(self):
        return "playing baseball takes 4 hr"
    
Basketball= Basketball()
Baseball= Baseball()

print(Baseball.play())
print(Basketball.play())