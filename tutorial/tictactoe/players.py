from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name):
        self.__name = name
        
    @property
    def name(self): return self.__name

    @abstractmethod
    def select(state, actions):
        """
            Выбирает действие среди доступных и возвращает его.
            
            Либо возвращает None, если игрок отказался от доступных действий
        """
        ...
        
        
class ConsolePlayer(Player):
    def select(self, state, actions):
        if len(actions) == 0:
            return None
        
        print("Player - %s" % self.name)
        print(state)
        for n, a in enumerate(actions):
            print(f'{n+1:2d}) {a.msg()}')
            
        print(f'Any other number to exit.')  
            
        while True:
            try:
                result = int(input("Please, enter a number: "))
            except:
                print("Try again")
                continue
            break
            
        return actions[result-1] if 0 < result <= len(actions) else None
    
    
class RandomAIPlayer(Player):
    def select(self, state, actions):
        import random 
        
        if len(actions) == 0:
            return None
        
        return random.choice(actions)
 