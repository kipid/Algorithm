function countSubstrings(s: string): number {
    let count = 0;
    
    // Helper function to count palindromes expanding from a center
    function countPalindromes(left: number, right: number): void {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            count++;  // Found a palindrome
            left--;   // Expand left
            right++;  // Expand right
        }
    }
    
    // Check each position as a potential center
    for (let i = 0; i < s.length; i++) {
        // Odd length palindromes (single character center)
        countPalindromes(i, i);
        
        // Even length palindromes (between two characters)
        countPalindromes(i, i + 1);
    }
    
    return count;
};