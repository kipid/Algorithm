function reverseBits(n: number): number {
	let w = n % 2;
    let ans = w;
    n = (n - w) / 2;
    for (let i = 1; i < 32; i++) {
        w = n % 2;
        ans = (ans << 1) + w;
        n = (n - w) / 2;
    }
    return ans >>> 0;
};