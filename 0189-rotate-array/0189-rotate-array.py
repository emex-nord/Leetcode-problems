class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swiper(lst,left,right):
            while right >left:
                lst[left],lst[right]=lst[right],lst[left]
                right-=1
                left+=1

        right_pointer=len(nums)-1
        left_pointer=0
        mid_pointer=k%len(nums)

        nums.reverse()
        swiper(nums,left_pointer,mid_pointer-1)
        swiper(nums,mid_pointer,right_pointer)
