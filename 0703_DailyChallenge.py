class Solution(object):
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        low = 0
        high = 1000000000000000

        def journey(mid):
            trip = 0
            for t in time:
                trip += (mid//t)
            return trip >= totalTrips

        while low <= high:
            mid = (low + high) >>1

            if journey(mid):
                if mid -1 ==0 or not journey(mid-1):
                    return mid
                high = mid -1

            else:
                low = mid + 1