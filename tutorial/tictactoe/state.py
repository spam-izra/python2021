from abc import ABC, abstractmethod

class Action(ABC):
    """
        Абстрактный класс, реализующий ход игрока
    """
    def __init__(self, msg):
        self.__msg = msg
        
    @abstractmethod
    def do(self):
        """
            Метод, который из текущего состояния создает новое
            на основе хода игрока
        """
        ...
        
    def msg(self):
        """
            Сообщение для пользователя
        """
        return self.__msg
        

class PutXOAndNextAction(Action):
    """
        Просто действие - помещает символ игрока в указанную клетку
    """
    def __init__(self, state, x, y):
        super().__init__(
            f'Put [{"X" if state.player == 1 else "O"}] in ({x:2d}, {y:2d})'
        )
        
        self.__state = state
        self.__x = x
        self.__y = y
        
    def do(self):
        board = self.__state.board
        board.set_cell(self.__x, self.__y, "X" if self.__state.player == 1 else "O")
        
        s = State(
            board=board, parent=self.__state,
            player=1 if self.__state.player == 2 else 2,
        )
        return s
    
class State:
    """
        Описывает текущее состояние игры
    """
    def __init__(self, *, M=3, board=None, player=1, parent=None):
        self.__parent = parent
        self.__player = player
        self.__board = board
        self.__M = M if parent is None else parent.__M
        
    @property
    def M(self):
        return self.__M
        
    @property
    def parent(self):
        return self.__parent
    
    @property
    def board(self):
        """
            Свойствой, которое позволяет обращаться к доске,
            но не позволяет ее сменить (очень дорошая реализация)
        """
        return self.__board.clone()
    
    @property
    def player(self):
        return self.__player
            
        
    def clone(self):
        """
            Создание клона
        """
        s = State(
            player=self.__player,
            board=self.__board.clone(), 
            parent=self.__parent)
        
        s.__player = self.__player
        return s
    
    def is_end(self):
        """
            Проверка на то, является ли это состояние конечным
        """
        winner = self.has_winner()
        if winner is not None:
            return True
        
        for _, value in self.__board.itercells():
            if value is None:
                return False
        return True
    
    def has_winner(self):
        """
            Ищем победителя
        """
        x_win = "X"*self.__M
        o_win = "O"*self.__M
        
        rows = list(self.__board.iterrows())
        cols = list(self.__board.itercols())
        diag1 = list(self.__board.iterdiag1())
        diag2 = list(self.__board.iterdiag2())
        
        for checks in [rows, cols, diag1, diag2]:
            for seq in checks:
                line = "".join([c if c is not None else "_" for _, c in seq])
                if x_win in line:
                    return "X"
                if o_win in line:
                    return "O"
                
        return None

    def get_actions(self):
        """
            Для простоты будем считать, что само состояние знает, как 
            породить новые состояния. Конкретное создание новых состояни
            делегирует специальному классу Action
            
            В нормальной реализации нужно вынести в отдельный объект,
            который реализует правила игры.
        """
        if self.is_end():
            return []
        
        actions = []
        for (x, y), cell in self.__board.itercells():
            if cell is None:
                actions.append(
                    PutXOAndNextAction(self, x, y)
                )
        return actions 
    
    def __str__(self):
        s =  f"Current player: [{'X' if self.__player == 1 else 'O'}]\n"
        s += str(self.__board)
        return s
    
    def __repr__(self):
        return self.__str__()
        