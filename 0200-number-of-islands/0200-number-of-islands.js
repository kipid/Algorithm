/**
 * @param {character[][]} grid
 * @return {number}
 */
const numIslands = function(grid) {
    const extendedGrid = [];
    const rowTop = ["0"];
    const rowBottom = ["0"];
    for (let i = 0; i < grid[0].length; i++) {
        rowTop[i+1] = "0";
        rowBottom[i+1] = "0";
    }
    rowTop.push("0");
    rowBottom.push("0");
    extendedGrid.push(rowTop);
    for (let i = 0; i < grid.length; i++) {
        let row = ["0"];
        for (let j = 0; j < grid[i].length; j++) {
            row[j+1] = grid[i][j];
        }
        row.push("0");
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