from .state import State

class Game:
    def __init__(self, player1, player2, *, board, M):
        self.__players = [None, player1, player2]
        self.__state = State(board=board, M=M)
        self.__init_state = self.__state.clone()
        
    def reset(self):
        self.__state = self.__init_state.clone()
        
    def start(self):
        while True:
            if self.__state.is_end(): 
                break

            actions = self.__state.get_actions()
            act = self.__players[self.__state.player].select(self.__state, actions)
            if act == None:
                break
            self.__state = act.do()

        print(self.__state)
        print("Winner: ", self.__state.has_winner())