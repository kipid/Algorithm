function longestPalindrome(s: string): string {
    if (s.length <= 1) { return s; }

    let start = 0;
    let maxLength = 1;

    const expandAroundCenter = (left: number, right: number): number => {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        return right - left - 1;
    }

    for (let i = 0; i < s.length; i++) {
        let len1 = expandAroundCenter(i, i);
        let len2 = expandAroundCenter(i, i+1);
        let currMaxLength = Math.max(len1, len2);
        if (currMaxLength > maxLength) {
            maxLength = currMaxLength;
            start = i - Math.floor((maxLength - 1) / 2);
        }
    }
    return s.substring(start, start + maxLength);
};