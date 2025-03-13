/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
    for (let i = 0; i < matrix.length - 1; i++) {
        for (let j = i + 1; j < matrix[i].length; j++) {
            let temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
    const k = Math.floor(matrix.length / 2);
    for (let j = 0; j < k; j++) {
        for (let i = 0; i < matrix.length; i++) {
            let temp = matrix[i][j];
            matrix[i][j] = matrix[i][matrix[j].length - 1 - j];
            matrix[i][matrix[j].length - 1 - j] = temp;
        }
    }
};