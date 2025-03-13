/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const map = new Map();
    
    for (let str of strs) {
        // Sort the characters of the string to create a key
        const sortedStr = str.split('').sort().join('');
        
        // If key exists, append to existing array, otherwise create new array
        if (map.has(sortedStr)) {
            map.get(sortedStr).push(str);
        } else {
            map.set(sortedStr, [str]);
        }
    }
    
    // Convert map values to array
    return Array.from(map.values());
};