class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(n) time, and O(h) space
        def binary_search(nums, t):
            center_i = len(nums) // 2
            center = nums[center_i]
            if center == t:
                return center_i
            elif len(nums) == 1:
                return center_i if t < center else center_i + 1
            elif t < center:
                return binary_search(nums[:center_i], t)
            else:
                return center_i + binary_search(nums[center_i:], t)

        #return binary_search(nums, target)

        # O(logn) time and O(h) space
        def binary_search_indices(l, r, t):    
            center_i = (l + r) // 2
            center = nums[center_i]
            if t == center:
                return center_i
            elif l == r:
                return l if nums[l] >= t else l + 1
            elif t < center:
                if l > center_i - 1:
                    return l
                index = binary_search_indices(l, center_i - 1, t) 
            else:
                if r < center_i - 1:
                    return r
                index = binary_search_indices(center_i + 1, r, t)

            return index

        #return binary_search_indices(0, len(nums) - 1, target)

        # Optimal: O(logn) time and O(1) space
        def binary_search_iter(nums, t):
            l, r = 0, len(nums) - 1
            while r >= l:
                m = (l + r) // 2
                if nums[m] == t:
                    return m
                #elif r == l:
                #    return l if nums[l] >= t else l + 1
                elif nums[m] > t:
                    r = m - 1
                else:
                    l = m + 1
            return l

        return binary_search_iter(nums, target)
    
if __name__ == "__main__":
    s = Solution()
    #index = s.searchInsert([1, 3, 5, 6], 7)
    #print(index)
    print(s.searchInsert([1, 3], 0))