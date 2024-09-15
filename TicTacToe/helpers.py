from os.path import isdir, join, basename

def flattenGrid(grid):
    gridAux = grid.copy()
    flattenedGrid = []
    while len(gridAux) != 0:
        row = gridAux.pop(0)
        while len(row) != 0:
            flattenedGrid.append(row.pop(0))
    return flattenedGrid

def loadAsset(name, dir):
    #CheckFileName (does not matter here cause name and dir are internally provided)....
    if not isdir(dir):
        raise NotADirectoryError(dir)
    assetStr = ""
    with open(join(dir,basename(name))) as fileAsset:
        for line in fileAsset:
            assetStr += line
        return assetStr