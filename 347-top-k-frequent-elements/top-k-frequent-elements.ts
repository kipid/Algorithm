class MinHeap {
    private heap: [number, number][];
    
    constructor() {
        this.heap = [];
    }
    
    private getParentIndex(index: number): number {
        return Math.floor((index - 1) / 2);
    }
    
    private getLeftChildIndex(index: number): number {
        return 2 * index + 1;
    }
    
    private getRightChildIndex(index: number): number {
        return 2 * index + 2;
    }
    
    private swap(i: number, j: number): void {
        [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
    }
    
    private heapifyUp(index: number): void {
        const parent = this.getParentIndex(index);
        if (index > 0 && this.heap[index][1] < this.heap[parent][1]) {
            this.swap(index, parent);
            this.heapifyUp(parent);
        }
    }
    
    private heapifyDown(index: number): void {
        const left = this.getLeftChildIndex(index);
        const right = this.getRightChildIndex(index);
        let smallest = index;
        
        if (left < this.heap.length && this.heap[left][1] < this.heap[smallest][1]) {
            smallest = left;
        }
        if (right < this.heap.length && this.heap[right][1] < this.heap[smallest][1]) {
            smallest = right;
        }
        
        if (smallest !== index) {
            this.swap(index, smallest);
            this.heapifyDown(smallest);
        }
    }
    
    insert(value: [number, number]): void {
        this.heap.push(value);
        this.heapifyUp(this.heap.length - 1);
    }
    
    extractMin(): [number, number] {
        const min = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        if (this.heap.length > 0) {
            this.heapifyDown(0);
        }
        return min;
    }
    
    size(): number {
        return this.heap.length;
    }
}

function topKFrequent(nums: number[], k: number): number[] {
    // Step 1: Count frequencies using Map
    const freqMap: Map<number, number> = new Map();
    for (const num of nums) {
        freqMap.set(num, (freqMap.get(num) || 0) + 1);
    }
    // Step 2: Convert to array of [number, frequency] pairs and sort
    const freqArray: [number, number][] = Array.from(freqMap.entries());
    freqArray.sort((a, b) => b[1] - a[1]); // Sort by frequency descending
    
    // Step 3: Take first k elements and extract numbers
    return freqArray.slice(0, k).map(([num]) => num);
};
