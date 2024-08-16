class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        extendedGrid = []
        rowTop = ["0"]
        rowBottom = ["0"]
        for i in range(0, len(grid[0])):
            rowTop.append("0")
            rowBottom.append("0")
        rowTop.append("0")
        rowBottom.append("0")
        extendedGrid.append(rowTop)
        for i in range(0, len(grid)):
            row = ["0"]
            for j in range(0, len(grid[i])):
                row.append(grid[i][j])
            row.append("0")
            extendedGrid.append(row)
        extendedGrid.append(rowBottom)

        numOfLands = 0
        def linkLands(i: int, j: int) -> None:
            nonlocal numOfLands
            if extendedGrid[i][j] == "1":
                numOfLands+=1
                extendedGrid[i][j] = "L" + str(numOfLands)

            if extendedGrid[i][j].startswith("L"):
                if extendedGrid[i-1][j] == "1":
                    extendedGrid[i-1][j] = "L" + str(numOfLands)
                    linkLands(i-1, j)
    
                if extendedGrid[i][j+1] == "1":
                    extendedGrid[i][j+1] = "L" + str(numOfLands)
                    linkLands(i, j+1)
    
                if extendedGrid[i+1][j] == "1":
                    extendedGrid[i+1][j] = "L" + str(numOfLands)
                    linkLands(i+1, j)
    
                if extendedGrid[i][j-1] == "1":
                    extendedGrid[i][j-1] = "L" + str(numOfLands)
                    linkLands(i, j-1)

        for i in range(1, len(extendedGrid)-1):
            for j in range(1, len(extendedGrid[i])-1):
                linkLands(i, j)

        return numOfLands