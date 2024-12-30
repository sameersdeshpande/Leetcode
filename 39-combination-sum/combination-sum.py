class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(start, path,target):
            if target ==0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate > target:
                    continue
                path.append(candidate)
                backtrack(i,path,target-candidate)
                path.pop()
        backtrack(0,[],target)
        return result