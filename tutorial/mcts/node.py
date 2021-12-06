from abc import ABC, abstractmethod
import sys
import math
import random

class MCTSNode(ABC):
    def __init__(self, *, parent=None):
        self.__parent = parent
        
        self.__score = {}
        self.__N = 0
        self.__childs = None
        
    @property
    def N(self):
        return self.__N
    
    @property
    def childs(self):
        return self.__childs
    
    @property
    def parent(self):
        return self.__parent
    
    def __str__(self):
        s = "[" + "/".join(["%5.2f" % self.__score[p] for p in sorted(self.__score)]) + ("] | %3d" % self.__N)
        if self.__childs is None:
            s += " | None"
        else:
            c = 0
            for child in self.__childs:
                if child is not None: c += 1
            s += " | %3d/%3d" % (c, len(self.__childs))
        return s
    
    def __repr__(self):
        return self.__str__()
    
    def score(self):
        if self.__parent is None:
            return -1
        
        if self.__N == 0:
            return sys.float_info.max
        
        return self.__score.get(self.__parent.player(), 0) / self.__N + math.sqrt(
            math.log(self.__parent.__N) / self.__N
        )
    
    def best_move(self):
        best = None
        best_N = None
        for n, child in enumerate(self.__childs):
            if best_N is None or best_N < child.__N:
                best = n
                best_N = child.__N
        return best
    
    def selection(self):
        if self.is_terminal():
            return self
        
        if self.__childs is None or len(self.__childs) == 0:
            return self
        
        best = None
        best_score= None
        for child in self.__childs:
            if child is None:
                return self
            score = child.score() 
            if best_score is None or score > best_score:
                best_score = score
                best = child
                
        return best.selection()
    
    def expansion(self):
        if self.is_terminal():
            return self
        
        if self.__childs is None:
            n = self.number_of_childs()
            self.__childs = [None for _ in range(n)]
            
        for i in range(len(self.__childs)):
            if self.__childs[i] is not None:
                continue
                
            self.__childs[i] = self.create_child(i)
            return self.__childs[i]
        
        raise Exception("Something bad happens")
    
    def backpropagation(self, score):
        for p in score:
            self.__score[p] = self.__score.get(p, 0) + score[p]
        self.__N += 1
        
        if self.__parent is not None:
            self.__parent.backpropagation(score)
    
    @abstractmethod
    def player(self):
        ...
        
    @abstractmethod
    def is_terminal(self):
        ...
      
    @abstractmethod
    def number_of_childs(self):
        ...
        
    @abstractmethod
    def create_child(self, n):
        ...
        
    @abstractmethod
    def simulation(self):
        ...