// 우선순위 큐 클래스 (한 번만 정의)
class PriorityQueue0 {
    private heap: number[];
    private isMax: boolean;

    constructor(isMax: boolean) {
        this.heap = [];
        this.isMax = isMax;
    }

    push(num: number): void {
        this.heap.push(num);
        this.bubbleUp(this.heap.length - 1);
    }

    pop(): number | undefined {
        if (this.heap.length === 0) return undefined;
        if (this.heap.length === 1) return this.heap.pop();

        const root = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this.bubbleDown(0);
        return root;
    }

    peek(): number | undefined {
        return this.heap[0];
    }

    size(): number {
        return this.heap.length;
    }

    private bubbleUp(index: number): void {
        while (index > 0) {
            const parent = Math.floor((index - 1) / 2);
            if (this.compare(this.heap[index], this.heap[parent])) {
                [this.heap[index], this.heap[parent]] = [this.heap[parent], this.heap[index]];
                index = parent;
            } else {
                break;
            }
        }
    }

    private bubbleDown(index: number): void {
        const n = this.heap.length;
        while (true) {
            let target = index;
            const left = 2 * index + 1;
            const right = 2 * index + 2;

            if (left < n && this.compare(this.heap[left], this.heap[target])) {
                target = left;
            }
            if (right < n && this.compare(this.heap[right], this.heap[target])) {
                target = right;
            }
            if (target === index) break;

            [this.heap[index], this.heap[target]] = [this.heap[target], this.heap[index]];
            index = target;
        }
    }

    private compare(a: number, b: number): boolean {
        return this.isMax ? a > b : a < b;
    }
}

// MedianFinder 클래스
class MedianFinder {
    private small; // 최대 힙
    private large; // 최소 힙

    constructor() {
        this.small = new PriorityQueue0(true);  // 최대 힙
        this.large = new PriorityQueue0(false); // 최소 힙
    }

    addNum(num: number): void {
        this.small.push(num);

        if (this.small.peek()! > (this.large.peek() ?? Infinity)) {
            this.large.push(this.small.pop()!);
        }

        if (this.small.size() > this.large.size() + 1) {
            this.large.push(this.small.pop()!);
        } else if (this.large.size() > this.small.size()) {
            this.small.push(this.large.pop()!);
        }
    }

    findMedian(): number {
        if (this.small.size() > this.large.size()) {
            return this.small.peek()!;
        }
        return (this.small.peek()! + this.large.peek()!) / 2;
    }
}

/**
 * 사용 예시:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */