from configs import GameConfig
from enums import GameState
MARK_CONFIG = GameConfig.OBJ_MARK

class GameObj:
    def __init__(self, mark, pos):
        self.pos = pos
        
        #print("Mark is: ", mark)
        if mark == MARK_CONFIG[1]:
            self._mark = 1
        elif mark == MARK_CONFIG[2]:
            self._mark = 2
        elif mark == "N/A":
            self._mark = 0
        else:
            self._mark = -1
            print("Invalid mark")
    
    def _xcoord(self):
        return self.pos[0]
    def _ycoord(self):
        return self.pos[1]
    
    xcoord = property(_xcoord)
    ycoord = property(_ycoord)

    def mark(self):
        if self._mark == 1:
            return MARK_CONFIG[1]
        elif self._mark == 2:
            return MARK_CONFIG[2]
        elif self._mark == 0:
            return MARK_CONFIG[0]
        else:
            return MARK_CONFIG[-1]

class Grid:
    def __init__(self, d):
        self._grid = []
        self.dim = d
        
    def add(self, obj):
        x = obj.xcoord
        y =  obj.ycoord
        
        if not (x < 0 or y < 0 or x > self.dim or y > self.dim):
            found = False
            i = 0
            
            while i < len(self._grid) and not found:
            
                objX = self._grid[i].xcoord
                if  objX > x :
                    found = True
                elif objX == x:
                    found = True

                else:
                    i += 1
                    
            found = False
            while i < len(self._grid) and not found:
                #X Found
                objY = self._grid[i].ycoord
                objX = self._grid[i].xcoord
                #Y Found
                if objX > x or (objX == x and objY > y):
                    found = True
                    
                #Obj already exists
                elif objX == x and objY == y:
                    #print("addError: posAlreadyFilled")
                    return False
                else:
                    i+=1  
                
            self._grid.insert(i, obj)
            return True
        else:
            print("addError: Position OutOfBounds")
            return False
                        
    
    def findInGrid(self, pos_l):
            found = False
            i = 0

            while not found and i < len(self._grid):
                if self._grid[i].xcoord == pos_l[0] and self._grid[i].ycoord == pos_l[1]:
                    found = True
                else: 
                    i+=1
                
            return i

    def getObj(self, pos):
        posInd = self.findInGrid(pos)
        #print("getObj: inPos: ", pos, "findInGridPosInd: ", posInd, "grid: ", self.grid )
        if posInd < len(self._grid):
            return self._grid[posInd]
        
        else:
            return GameObj(MARK_CONFIG[-1], pos)
    
    def getByMark(self, mark):
        return filter(lambda obj: isinstance(obj, GameObj) and obj.mark == mark, self._grid)
    
    def reset(self):
        self._grid = []       
        
    def getGrid(self):
        EMPTY_SPACE_MARK = " "
        matrix = [[EMPTY_SPACE_MARK for i in range(self.dim)] for j in range(self.dim)]  
        
        for gameObj in self._grid:
            row = gameObj.xcoord
            col = gameObj.ycoord
            mark = gameObj.mark()
            matrix[row][col] = mark

        return matrix
    
    def over(self):
        DIAG_COORDS = {(0,0), (1,1), (2,2)}
        ANTI_DIAG_COORDS = {(2,2), (2,0), (0,2)}
        VERTICAL_COORDS = tuple({(i,j) for i in range(3)} for j in range(3))
        HORIZONTAL_COORDS = tuple({(i,j) for j in range(3)} for i in range(3))
        #obj_list = filter(lambda gameObj: gameObj.mark, self.getGrid()
        playerOneMoves = {(gameObj.xcoord, gameObj.ycoord) for gameObj in self._grid if gameObj.mark() == MARK_CONFIG[1]}
        playerTwoMoves = {(gameObj.xcoord, gameObj.ycoord) for gameObj in self._grid if gameObj.mark() == MARK_CONFIG[2]}

        if len(self._grid) == 9:
            return GameState.DRAW
        
        elif (DIAG_COORDS.issubset(playerOneMoves) or 
            ANTI_DIAG_COORDS.issubset(playerOneMoves) or 
            any(V_WIN_COND.issubset(playerOneMoves) for V_WIN_COND in VERTICAL_COORDS) or
            any(H_WIN_COND.issubset(playerOneMoves) for H_WIN_COND in HORIZONTAL_COORDS)):
            return GameState.PLAYER_ONE_WINS
        
        elif (DIAG_COORDS.issubset(playerTwoMoves) or 
            ANTI_DIAG_COORDS.issubset(playerTwoMoves) or 
            any(V_WIN_COND.issubset(playerTwoMoves) for V_WIN_COND in VERTICAL_COORDS) or
            any(H_WIN_COND.issubset(playerTwoMoves) for H_WIN_COND in HORIZONTAL_COORDS)):
            return GameState.PLAYER_TWO_WINS
        
        else:
            return GameState.ONGOING
            
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