class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=[]
        k=k%len(nums)
        for i in range(1,k+1):
            s.append(nums[-i])
        hi=s[::-1]
        for i in range(len(nums)-k):
            hi.append(nums[i])
        nums[:]=hi