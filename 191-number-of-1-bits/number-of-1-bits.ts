function hammingWeight(n: number): number {
    let sum = n % 2;
    n = (n - n % 2) / 2;
    while (n > 0) {
        sum += n % 2;
        n = (n - n % 2) / 2;
    }
    return sum;
};