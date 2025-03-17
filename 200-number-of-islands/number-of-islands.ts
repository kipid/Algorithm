function numIslands(grid: string[][]): number {
    function fillLand(i: number, j: number) {
        if (grid[i][j] === "1") {
            grid[i][j] = "0";
            if (i < grid.length - 1) { fillLand(i+1, j) }
            if (j < grid[i].length - 1) { fillLand(i, j+1) }
            if (i > 0) { fillLand(i-1, j) }
            if (j > 0) { fillLand(i, j-1) }
        }
    }
    
    let count = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === "1") {
                count++;
                fillLand(i, j);
            }
        }
    }
    return count;
};