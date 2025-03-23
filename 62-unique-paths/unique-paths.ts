const numOfPaths = [[1, 1],
                    [1]]
function uniquePaths(m: number, n: number): number {
    for (let i = 2; i < m; i++) {
        numOfPaths[i] = [1];
    }
    for (let i = 0; i < m; i++) {
        for (let j = 1; j < n; j++) {
            numOfPaths[i][j] = (numOfPaths[i-1]?.[j] ?? 0) + numOfPaths[i][j-1];
        }
    }
    return numOfPaths[m-1][n-1];
};