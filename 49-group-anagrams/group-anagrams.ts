function groupAnagrams(strs: string[]): string[][] {
    const map = new Map<string, string[]>();
    for (let i = 0; i < strs.length; i++) {
        const sortedStr = strs[i].split("").sort().join("");
        if (map.has(sortedStr)) {
            map.get(sortedStr).push(strs[i]);
        } else {
            map.set(sortedStr, [strs[i]]);
        }
    }
    return Array.from(map.values());
};