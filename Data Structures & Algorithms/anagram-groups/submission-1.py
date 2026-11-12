class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        V = defaultdict(list)
        for s in strs:
            SO = ''.join(sorted(s))
            V[SO].append(s)
        return list(V.values())
        
            

