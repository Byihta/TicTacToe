import logging
from os import system
from structures import GameObj, Grid, Event, GameEvent, Logger
import queue
from configs import GameConfig
from enums import GameState
from helpers import flattenGrid, loadAsset
from sys import stdout
from sys import exit as sys_exit


""" class EventController():
    eventHandler = {}
    def __init__(self):
        self.queue = queue.Queue()
        
    
    def add(self, event):
        self.queue.put(event)    
    
    def addCallback(kind, callback):
        
        if not (kind in EventController.eventHandler) and callback != None:
            EventController.eventHandler[kind] = callback
        
        else:
            logging.error("Event handler - Callback to event kind already registered")
            
            
    def consume(self, id):
        e = None
        try:
            e = self.queue.get_nowait()
        except queue.Empty:
            logging.error("EventController - Attempted to get event from empty EventQueue")
        return e
    
    def reset(self):
        self.queue = queue.Queue()
    
    def handle(self):
        #TypeChecking
        eventHandler = {"initialiseGame": GameController.initialiseGame,
                        "checkGameOver": GameController.checkGameOver,
                        "playTurn": GameController.playTurn}
        kind = self.kind
        
        if not (kind in eventHandler):
            logging.error("EventController - No event handler found for this kind")
        try:
            handlerProcedure = eventHandler[self.kind]
            handlerProcedure()
        except :
            logging.error("EventController - Error in Event Handling")
#Runs the Game itself, as a backend """



class GameController():
    def __init__(self):
        self.Grid = Grid(3)
        #self.EventController = EventController()
        self.UI = UIController
        self.Player = 1
        #Change player1 always goes first

    def initGame(self):
        self.Grid.reset()
        #self.EventController.reset()
    
    def runMainLoop(self):
        over = False
        while not over:
            self.UI.updateScreen(self.UI.gameScreen(self.Grid.getGrid(), self.Player))
            self.playTurn()
            over = self.resolveGameState()

    def switchPlayer(self):
        self.Player = self.Player % 2 + 1

    def playTurn(self):
        turnPlayed = False
        interactionStr = "Where to put mark:\n"
        while not turnPlayed:
            #Check for invalid input
            userInput = input(interactionStr).split(' ', 1)
            if len(userInput) != 2 or any(not digit.isdigit() for digit in userInput):
                interactionStr = "Invalid user input, positions must be in format 'x y':\n"
                stdout.write("\033[A\033[K\033[A\033[K")
                continue

            pos = tuple(map(int, userInput))
            turnPlayed = self.Grid.add(GameObj(GameConfig.OBJ_MARK[self.Player], pos))
            if not turnPlayed:
                interactionStr = "Invalid position. Try again:\n"
                stdout.write("\033[A\033[K\033[A\033[K")

        #print(f"pos = {pos[0]}, {pos[1]}")

    def resolveGameState(self):
        state = self.Grid.over()
        match state:
            case GameState.ONGOING:
                self.switchPlayer()
                return False
            case _:
                self.endGame(state)
                return True
    
    def endGame(self, state):
        self.UI.updateScreen(self.UI.gameOverScreen(state))
        
class UIController():
    def gameScreen(grid, player):
        def aux():
            flattenedGrid = flattenGrid(grid)
            header = 57*" "+ f"Player {player}\n"
            bodyStr = loadAsset("grid", "assets")
            for i in range(9):
                bodyStr = bodyStr.replace(str(i), flattenedGrid[i])
            print(header, bodyStr)
            return None
        return aux
    
    def gameOverScreen(state):
        def aux():
            match state:
                case GameState.PLAYER_ONE_WINS:
                    print(loadAsset("oneWins", "assets/gameOver"))
                case GameState.PLAYER_TWO_WINS:
                    print(loadAsset("twoWins", "assets/gameOver"))
                case GameState.DRAW:
                    print(loadAsset("draw", "assets/gameOver"))
            input()
            return None
        return aux

    def clearScreen():
        system('cls')

    def updateScreen(screen):
        UIController.clearScreen()
        option = screen()
        return int(option) if option is not None else None
    
    def mainMenuScreen():
        print("Welcome to console Tic Tac Toe:")
        print("1 - Play")
        print("2 - Exit")
        option = input("Select your option...\n")
        #print(f"You picked {option}") 
        return option
    
class Controller():
    #Opens the menu and runs the game
    #PlayGame
    #Exit

    #def __init__(self, frontend):
    #    self.frontend = frontend
    def run(self):
        while True:
            option = UIController.updateScreen(UIController.mainMenuScreen)
            match option:
                case 1:
                    g = GameController()
                    g.initGame()
                    g.runMainLoop()

                case 2:
                    UIController.clearScreen()
                    sys_exit(0)
            




