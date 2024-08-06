function longestCommonPrefix(strs: string[]): string {
    let minLength: number = Infinity;
    for (let str of strs) {
        minLength = Math.min(minLength, str.length);
    }
    for (let i = 0; i < minLength; i++) {
        let letter: string = strs[0].charAt(i);
        let same: boolean = true;
        for (let j = 1; j < strs.length; j++) {
            if (letter !== strs[j].charAt(i)) {
                same = false;
                break;
            }
        }
        if (!same) {
            return strs[0].substring(0, i);
        }
    }
    return strs[0].substring(0, minLength);
};
