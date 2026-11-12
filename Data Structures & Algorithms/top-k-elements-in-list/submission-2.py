class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencia = {}

        for i in nums:
            frequencia[i] = frequencia.get(i, 0) + 1

        nums_ordenados = sorted(frequencia, 
        key=lambda i: frequencia[i],
        reverse=True)

        return nums_ordenados[:k]
