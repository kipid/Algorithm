function exist(board: string[][], word: string): boolean {
    const m = board.length;
    const n = board[0].length;
    const visited = new Set<string>();
    
    // Helper function for DFS
    function dfs(row: number, col: number, index: number): boolean {
        // Base case: if we've matched all characters
        if (index === word.length) {
            return true;
        }
        
        // Check boundaries and if current cell matches current character
        if (
            row < 0 || row >= m ||
            col < 0 || col >= n ||
            visited.has(`${row},${col}`) ||
            board[row][col] !== word[index]
        ) {
            return false;
        }
        
        // Mark current cell as visited
        visited.add(`${row},${col}`);
        
        // Check all four directions
        const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        for (const [dr, dc] of directions) {
            if (dfs(row + dr, col + dc, index + 1)) {
                return true;
            }
        }
        
        // Backtrack: remove current cell from visited
        visited.delete(`${row},${col}`);
        
        return false;
    }
    
    // Try starting from each cell
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (dfs(i, j, 0)) {
                return true;
            }
        }
    }
    
    return false;
};