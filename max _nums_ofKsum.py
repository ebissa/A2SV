def maxOperations(self, nums: List[int], k: int) -> int:
            ans = 0
            if not nums or len(nums) == 1:
                return ans
            nums.sort()
            l = 0
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == k:
                    ans += 1
                    l +=1
                    r -=1
                elif s > k:
                    r -= 1
                else:
                    l += 1
            return ans
