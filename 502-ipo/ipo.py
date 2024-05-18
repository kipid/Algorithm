class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(nlargest(k, profits))
        
        projects = [[capital[i],profits[i]] for i in range(len(profits))]
        projects.sort(key=lambda x: x[0])
        
        heap = []
        
        for i in range(k):
            while projects and projects[0][0] <= w:
                heappush(heap, -projects.pop(0)[1]) # -를 넣어서 최대값이 처음으로 오도록 heapify.
            
            if not heap:
                break
            p = -heappop(heap) # capital 이 w 한도내의 최대 profit.
            w += p
        return w