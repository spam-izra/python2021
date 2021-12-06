from .board import Board

class SquareBoard(Board):
    """
        Квадратная доска
    """
    
    def __init__(self, N):
        self.__N = N
        self.__board = [
            [None for _ in range(self.__N)]
            for _ in range(self.__N)
        ]
        
    def clone(self):
        import copy
        b = SquareBoard(self.__N)
        b.__board = copy.deepcopy(self.__board)
        return b
    
    def get_cell(self, x, y):
        if not(0 < x <= self.__N) or not(0 < x <= self.__N):
            raise Exception("Too big or too low x/y")
            
        return self.__board[y-1][x-1]
        
    def set_cell(self, x, y, cell):
        if not(0 < x <= self.__N) or not(0 < y <= self.__N):
            raise Exception("Too big or too low x/y")
            
        if cell not in [None, "X", "O"]:
            raise Exception("Not valid value")

            
        self.__board[y-1][x-1] = cell
        
    def itercells(self):
        for ry in range(self.__N):
            for rx in range(self.__N):
                yield ((rx+1, ry+1), self.__board[ry][rx])
                
                
    def iterrows(self):
        for ry, row in enumerate(self.__board):
            yield [ ((rx+1, ry+1), value) for rx, value in enumerate(row) ]
        
    def itercols(self):
        for rx in range(self.__N):
            yield [ ((rx+1, ry+1), self.__board[ry][rx]) for ry in range(self.__N) ]
            
    def iterdiag1(self):
        diag = {}
        for (x, y), _ in self.itercells():
            d = x - y
            diag[d] = diag.get(d, []) + [(x, y)]
        
        for k in sorted(diag):
            yield [ ((x, y), self.__board[y-1][x-1]) for x, y in diag[k] ]

    def iterdiag2(self):
        diag = {}
        for (rx, ry), _ in self.itercells():
            d = (self.__N - 1 - rx) - ry
            diag[d] = diag.get(d, []) + [(rx, ry)]
        
        for k in sorted(diag):
            yield [ ((x, y), self.__board[y-1][x-1]) for x, y in diag[k] ]
                 
    def __str__(self):
        s =  "\n     " + " ".join(["%3d" % (col+1) for col in range(self.__N)]) + "\n" 
        s += "     " + "--- " * self.__N + "\n"
        for n, row in enumerate(self.__board):
            s += " %2d |" % (n+1)  + "".join([
                " %s |" % (v if v is not None else " ") for v in row
            ]) + "\n" 
            s += "     " + "--- " * self.__N + "\n"
        s += "\n"
        
        return s
    
    def __repr__(self):
        return self.__str__()