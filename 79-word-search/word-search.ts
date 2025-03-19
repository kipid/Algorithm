function exist(board: string[][], word: string): boolean {
    const m = board.length;
    const n = board[0].length;
    
    // 첫 글자가 일치하는 위치에서만 탐색 시작
    function findWord(row: number, col: number, index: number): boolean {
        // 모든 글자를 찾은 경우
        if (index === word.length) return true;
        
        // 경계 체크 및 글자 일치 여부 확인
        if (
            row < 0 || row >= m ||
            col < 0 || col >= n ||
            board[row][col] !== word[index]
        ) return false;
        
        // 현재 셀 임시로 마킹 (재사용 방지)
        const temp = board[row][col];
        board[row][col] = '#';
        
        // 네 방향 탐색 (단락 평가 사용)
        const found = 
            findWord(row, col + 1, index + 1) ||
            findWord(row + 1, col, index + 1) ||
            findWord(row, col - 1, index + 1) ||
            findWord(row - 1, col, index + 1);
        
        // 백트래킹: 원래 값 복원
        board[row][col] = temp;
        
        return found;
    }
    
    // 첫 글자와 일치하는 셀에서만 탐색 시작
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === word[0] && findWord(i, j, 0)) {
                return true;
            }
        }
    }
    
    return false;
};