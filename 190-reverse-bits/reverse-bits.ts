// function reverseBits(n: number): number {
// 	let w = n % 2;
//     let ans = w;
//     n = (n - w) / 2;
//     for (let i = 1; i < 32; i++) {
//         w = n % 2;
//         ans = (ans << 1) + w;
//         n = (n - w) / 2;
//     }
//     return ans >>> 0;
// };

function reverseBits(n: number): number {
    let result = 0;
    
    // Process all 32 bits
    for (let i = 0; i < 32; i++) {
        // Left shift result by 1 to make room for next bit
        result <<= 1;
        
        // Add the least significant bit of n to result
        result |= (n & 1);
        
        // Right shift n to process next bit
        n >>>= 1;  // Use >>> for unsigned right shift
    }
    
    return result >>> 0;  // Ensure unsigned 32-bit integer
}