
from typing import List


def binary_search(nums: List[int], target: int) -> int:

    left = 0
    right = len(nums) - 1

    while(left < right): 
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1 
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    
    return -1 

print(binary_search([-1,0,3,5,9,12], 9))