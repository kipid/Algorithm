function hammingWeight(n: number): number {
    let w = n % 2;
    let sum = w;
    n = (n - w) / 2;
    while (n > 0) {
        w = n % 2;
        sum += w;
        n = (n - w) / 2;
    }
    return sum;
};