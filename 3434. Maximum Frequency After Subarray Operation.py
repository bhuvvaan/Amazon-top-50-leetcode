class Solution:
    def maxFrequency(self, nums, k):

        
        counter = Counter(nums)
        num_k = counter[k]
        final = num_k

        for i in counter:

            if i == k:
                continue

            res = 0
            count = 0

            for j in nums:
                if i == j:
                    count += 1
                if j == k:
                    count -= 1

                if count < 0:
                    count = 0
                
                res = max(res, count)

            final = max(final, res + num_k)

        return final
