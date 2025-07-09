class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        queue = deque([(startGene,0)])
        visited = set([startGene])
        genes = ['A','C','G','T']

        while queue:
            current, mutations = queue.popleft()
            if current == endGene:
                return mutations
            for i in range(len(current)):
                for g in genes:
                    if current[i]!= g:
                        mutated = current[:i] + g + current[i+1:]     
                        if mutated in bank_set and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated, mutations+1))
        return -1  