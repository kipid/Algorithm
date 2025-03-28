/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = function(strs) {
    let minLength = Infinity;
    for (let str of strs) {
        minLength = Math.min(minLength, str.length);
    }
    for (let i = 0; i < minLength; i++) {
        let letter = strs[0].charAt(i);
        let same = true;
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