function isPalindrome(s: string): boolean {
    let sChanged = s.toLowerCase().replace(/[^a-z0-9]/g, "");
    return sChanged === sChanged.split("").toReversed().join("");
};