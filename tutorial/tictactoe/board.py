from abc import ABC, abstractmethod

class Board(ABC):
    """
        Интерфейс доски для игры. У каждой клетки есть своя координата.
        
        x - по горизонтали слева направо
        y - по вертикали сверху вниз
        
        Координата верхней левой клетки (1, 1)
    """
    
    @abstractmethod
    def clone(self):
        """
            Метод для создания копии доски
        """
        ...
    
    @abstractmethod
    def get_cell(self, x, y):
        """
            Получить значение в клетке по координатам
        """
        ...
        
    @abstractmethod
    def set_cell(self, x, y, cell):
        """
            Выставить значение в клетке по координатам
        """
        ...
      
    @abstractmethod
    def itercells(self):
        """
            Пройтись в клеткам по порядку - слева направо, сверху вниз
            
            То есть сначала выводится первая строка, потом вторая и т.д.
        """
        ...
                
    
    @abstractmethod
    def iterrows(self):
        """
            Пройтись по строкам сверху вниз
        """
        ...
       
    @abstractmethod
    def itercols(self):
        """
            Пройтись по столбцам слева направо
        """
        ...
        
    @abstractmethod
    def iterdiag1(self):
        """
            Пройтись по главным диагоналям
        """
        ...

    @abstractmethod
    def iterdiag2(self):
        """
            Пройтись по побочным диагоналям
        """
        ...
            