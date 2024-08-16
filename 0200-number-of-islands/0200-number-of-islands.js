/**
 * @param {character[][]} grid
 * @return {number}
 */
const numIslands = function(grid) {
    const extendedGrid = [];
    const rowTop = [];
    const rowBottom = [];
    for (let i = 0; i < grid[0].length; i++) {
        rowTop[i] = "0";
        rowBottom[i] = "0";
    }
    rowTop.splice(0, 0, "0");
    rowTop.splice(rowTop.length, 0, "0");
    rowBottom.splice(0, 0, "0");
    rowBottom.splice(rowBottom.length, 0, "0");
    extendedGrid.push(rowTop);
    for (let i = 0; i < grid.length; i++) {
        let row = [];
        for (let j = 0; j < grid[i].length; j++) {
            row[j] = grid[i][j];
        }
        row.splice(0, 0, "0");
        row.splice(row.length, 0, "0");
        extendedGrid.push(row);
    }
    extendedGrid.push(rowBottom);

    let numOfLands = 0;
    const linkLands = function (i, j) {
        if (extendedGrid[i][j] === "1") {
            numOfLands++;
            extendedGrid[i][j] = `land-${numOfLands}`;
        }
        if (extendedGrid[i][j].startsWith("land-")) {
            if (extendedGrid[i-1][j] === "1") {
                extendedGrid[i-1][j] = `land-${numOfLands}`;
                linkLands(i-1, j);
            }
            if (extendedGrid[i][j+1] === "1") {
                extendedGrid[i][j+1] = `land-${numOfLands}`;
                linkLands(i, j+1);
            }
            if (extendedGrid[i+1][j] === "1") {
                extendedGrid[i+1][j] = `land-${numOfLands}`;
                linkLands(i+1, j);
            }
            if (extendedGrid[i][j-1] === "1") {
                extendedGrid[i][j-1] = `land-${numOfLands}`;
                linkLands(i, j-1);
            }
        }
    }
    for (let i = 1; i < extendedGrid.length - 1; i++) {
        for (let j = 1; j < extendedGrid[i].length - 1; j++) {
            linkLands(i, j);
        }
    }
    return numOfLands;
};