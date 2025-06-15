import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:

        count = Counter(s)

        for value in count.values():
            if value > (len(s) + 1)//2:
                return ""

        heap = [(-cnt, chr) for chr, cnt in count.items()]
        heapq.heapify(heap)

        prev = (0,"")

        result = ""

        while heap:
            cnt, chr = heapq.heappop(heap)
            cnt += 1
            result += chr

            if prev[0] < 0:
                heapq.heappush(heap, prev)

            prev = (cnt, chr)

        return result

            

