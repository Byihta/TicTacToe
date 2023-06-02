import logging
from os import system
class gameObj:
    def __init__(self, mark, pos):
        print("Mark is: ", mark)
        if mark == "o":
            self.mark = 1
        elif mark == "x":
            self.mark = 2
        elif mark == '"N/A"':
            self.mark = 0
        else:
            self.mark = -1
            print("Invalid mark")
        
        self.pos = pos
    
    def getX(self):
        return self.pos[0]
    def getY(self):
        return self.pos[1]
    
    def getMark(self):
        if self.mark == 1:
            return "o"
        elif self.mark == 2:
            return "x"
        elif self.mark == 0:
            return " "
        else:
            return "?"
        



class Grid:
    
    def __init__(self, d):
        self.grid = []
        self.dim = d
        
    
    def add(self, obj):
        x = obj.getX()
        y =  obj.getY()
        
        if not (x < 0 or y < 0 or x > self.dim or y > self.dim):
            found = False
            i = 0
            
            while i < len(self.grid) and not found:
            
                objX = self.grid[i].getX()
                if  objX > x :
                    found = True
                elif objX == x:
                    found = True

                else:
                    i += 1
                    
            found = False
            while i < len(self.grid) and not found:
                #X Found
                objY = self.grid[i].getY()
                objX = self.grid[i].getX()
                #Y Found
                if objX > x or (objX == x and objY > y):
                    found = True
                    
                #Obj already exists
                elif objX == x and objY == y:
                    print("addError: posAlreadyFilled")
                else:
                    i+=1  
                
            self.grid.insert(i, obj)
        else:
            print("addError: Position OutOfBounds")
                        
    
    def findInGrid(self, pos_l):
            found = False
            i = 0

            while not found and i < len(self.grid):
                if self.grid[i].getX() == pos_l[0] and self.grid[i].getY() == pos_l[1]:
                    found = True
                else: 
                    i+=1
                
            return i

    def getObj(self, pos):
        
        posInd = self.findInGrid(pos)
        #print("getObj: inPos: ", pos, "findInGridPosInd: ", posInd, "grid: ", self.grid )
        if posInd < len(self.grid):
            return self.grid[posInd]
        
        else:
            return gameObj("N/A", pos)
    
    def reset(self):
        self.grid = []       
        
    def getGrid(self):
        
        EMPTY_SPACE_MARK = " "
        matrix = []  
        
        grid_i = 0 
        
        for row_i in range(self.dim):
            
            auxLine = []
            
            for col_i in range(self.dim):
                
                xInGrid = self.grid[grid_i].getX()
                yInGrid = self.grid[grid_i].getY()
                
                if row_i == xInGrid and col_i == yInGrid:
                    auxLine.append(self.grid[grid_i].getMark())
                    grid_i += 1
                    
                    
                else:
                    auxLine.append(EMPTY_SPACE_MARK)
            
            matrix.append(auxLine)
        
        return matrix
    
class Event():
    def __init__(self, kind, **kwargs):
        self.kind = kind
        
    def kind(self, eventKind = None):
        if eventKind:
            self.kind = eventKind
            return eventKind
        else:
            return self.kind

class GameEvent(Event):
    def __init__(self, kind, player = None):
        super().__init__(kind)
        self.player = player
        
    def player(self, eventPlayer = None):
        if eventPlayer:
            self.player = eventPlayer
        return self.player

    
            
    #Play Player1->CheckCondition-> Play Player2 ->
    #Kind, args

class Logger():
    def __init__(self, func):
        self.loggerFunc = func
        
    def log(self, message):
        self.loggerFunc(message)

class EventController():
    eventHandler = {}
    def __init__(self):
        self.queue = []
    
    def add(self, event):
        self.queue.append(event)    
    
    def addCallback(kind, callback):
        
        if not (kind in eventHandler) and callback != None:
            eventHandler[kind] = callback
        
        else:
            logging.error("Event handler - Callback to event kind already registered")
    def event(self, id):
        e = None
        try:
            e = self.queue[id]
        except IndexError:
            logging.error("EventController - Event not found")
        return e
        
    def handle(self):
        #TypeChecking
        eventHandler = {"checkGameOver": checkGameOver,
                        "playTurn": playTurn}
        kind = self.kind
        
        if not (kind in eventHandler):
            logging.error("EventController - No event handler found for this kind")
        try:
            handlerProcedure = eventHandler[self.kind]
            handlerProcedure()
        except :
            logging.error("EventController - Error in Event Handling")
#Runs the Game itself, as a backend
class GameController():
    def __init__(self):
        self.Grid = Grid()
        #Change player1 always goes first

        
class FrontEnd():
    def printGrid(self):
            matrix = self.getGrid()
            for row in matrix:
                rowStr = "|"
                
                for mark in row:
                    rowStr += mark
                rowStr += "|"
                print(rowStr)
    
class Controller():
    #Opens the menu and runs the game
    #PlayGame
    #Exit

    #def __init__(self, frontend):
    #    self.frontend = frontend
    def run():
        print("Welcome to console Tic Tac Toe:")
        print("1 - Play")
        print("2 - Exit")
        option = input("Select your option...\n")
        #Clear Screen
        if option == 0:
            pass