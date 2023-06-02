from models import Grid, gameObj

g = Grid(3)

pos1 = (1,0)
pos2 = (1,1)
pos3 = (0,0)
pos4 = (2,2)
pos5 = (1,2)
pos6 = (0,2)

p1 = gameObj('x', pos1)
p2 = gameObj('o', pos2)
p3 = gameObj('x', pos3)
print(p3.getMark())
p4 = gameObj('o', pos4)
p5 = gameObj('x', pos5)
p6 = gameObj('o', pos6)

m = [["x", " ", "o"],
     ["x", "o", "x"],
     [" ", " ", "o"]]

print("g.grid: ", [(g.grid[i].getX(),g.grid[i].getY(), g.grid[i].getMark()) for i in range(len(g.grid))])
g.add(p1)
print("g.grid: ", [(g.grid[i].getX(),g.grid[i].getY(), g.grid[i].getMark()) for i in range(len(g.grid))])
g.add(p2)
print("g.grid: ", [(g.grid[i].getX(),g.grid[i].getY(), g.grid[i].getMark()) for i in range(len(g.grid))])
g.add(p3)
print("g.grid: ", [(g.grid[i].getX(),g.grid[i].getY(), g.grid[i].getMark()) for i in range(len(g.grid))])
g.add(p4)
print("g.grid: ", [(g.grid[i].getX(),g.grid[i].getY(), g.grid[i].getMark()) for i in range(len(g.grid))])
g.add(p5)
print("g.grid: ", [(g.grid[i].getX(),g.grid[i].getY(), g.grid[i].getMark()) for i in range(len(g.grid))])
g.add(p6)
print("g.grid: ", [(g.grid[i].getX(),g.grid[i].getY(), g.grid[i].getMark()) for i in range(len(g.grid))])


if g.getObj(pos1) == p1:
    print("Test 1: Cleared")
else:
    print("Test 1: Failed: posReturned is: ", g.getObj(pos1))

if g.getObj(pos2) == p2:
    print("Test 2: Cleared")
else:
    print("Test 2: Failed: posReturned is: ", g.getObj(pos2))
    
if g.getObj(pos3) == p3:
    print("Test 3: Cleared")
else:
    print("Test 3: Failed: posReturned is: ", g.getObj(pos3))
    
if g.getObj(pos4) == p4:
    print("Test 4: Cleared")
else:
    print("Test 4: Failed: posReturned is: ", g.getObj(pos4))
    
    
    
matrix = g.getGrid()

if matrix == m:
    print("Test 5: Cleared")
else:
    print("Test 5 Failed: ")
    print("Grid is: ", matrix)
    print("Grid wanted is: ", m)

print("Test 6 printGrid:\n\n\n\n")
g.printGrid()
    


    