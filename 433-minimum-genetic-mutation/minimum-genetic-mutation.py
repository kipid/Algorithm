class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        geneDict = defaultdict(list)
        n = len(startGene)
        for i in range(n):
            geneDict[startGene[:i]+"*"+startGene[i+1:]].append(startGene)
        for gene in bank:
            for i in range(n):
                geneDict[gene[:i]+"*"+gene[i+1:]].append(gene)
        visited = set([startGene])
        q = deque([(startGene, 0)])
        while q:
            gene, count = q.popleft()
            if gene == endGene:
                return count
            for i in range(n):
                for nextGene in geneDict[gene[:i]+"*"+gene[i+1:]]:
                    if nextGene not in visited:
                        if nextGene == endGene:
                            return count + 1
                        visited.add(nextGene)
                        q.append((nextGene, count + 1))
        
        return -1