def solve():
    def work(start_idx, end_idx):
        if start_idx == end_idx:
            if (val := nums[start_idx]) > work.greatest_sum:
                work.greatest_sum = val
            return val, val, val

        pivot_idx = start_idx + (end_idx - start_idx) // 2
        val_left_sum_left,  val_left_sum_whole,  val_left_sum_right = work(start_idx, pivot_idx)
        val_right_sum_left,  val_right_sum_whole,  val_right_sum_right = work(pivot_idx + 1, end_idx)

        whole = val_left_sum_whole + val_right_sum_whole
        left = max(val_left_sum_left, val_left_sum_whole, val_left_sum_whole + val_right_sum_left, whole)
        right = max(whole, val_left_sum_right + val_right_sum_whole, val_right_sum_whole, val_right_sum_right)

        if (max_ := max(left, whole, right, val_left_sum_right + val_right_sum_left)) > work.greatest_sum:
            work.greatest_sum = max_

        return left, whole, right

    f = open('user.out', 'w')
    for nums in map(loads, stdin):
        # work.greatest_sum = -10001
        # work(0, len(nums) - 1)
        # print(work.greatest_sum, file=f)

        # Faster O(n) solution:
        top_sum, current_sum = -10001, 0
        for num in nums:
            current_sum += num
            if current_sum > top_sum:
                top_sum = current_sum
            if current_sum < 0:
                if num > top_sum:
                    top_sum = num
                current_sum = 0

        print(top_sum, file=f)

# sys.setrecursionlimit(50000)
solve()
exit()