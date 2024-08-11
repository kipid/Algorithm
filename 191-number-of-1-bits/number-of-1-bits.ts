function hammingWeight(n: number): number {
    let w: number = 0;
    while (n > 0) {
        w += n % 2;
        n = Math.floor(n / 2);
    }
    return w;
};