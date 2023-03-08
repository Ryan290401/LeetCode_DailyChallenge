"""
l, r = left, right
pk = predicted value k
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        pk = r

        while l <= r:
            k = (1 + r) // 2
            hours= 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                pk = min(pk,k)
                r = k-1
            else:
                l = k+1

        return pk