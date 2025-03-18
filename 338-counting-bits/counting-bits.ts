function countBits(n: number): number[] {
    const singleCountBits = (k: number): number => {
        let w = k % 2;
        let sum = w;
        k = (k - w) / 2;
        while (k > 0) {
            w = k % 2;
            sum += w;
            k = (k - w) / 2;
        }
        return sum;
    }
    const res = [];
    for (let i = 0; i <= n; i++) {
        res.push(singleCountBits(i));
    }
    return res;
};