/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    let w = 0;
    while (n > 0) {
        w += n % 2;
        n = Math.floor(n / 2);
    }
    return w;
};