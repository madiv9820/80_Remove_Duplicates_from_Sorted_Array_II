from typing import List
from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Create a frequency dictionary to count occurrences of each number in nums
        frequency_Dict = Counter(nums)
        actual_Index = 0  # This will track the position to place unique numbers in nums

        # Iterate through each unique number and its frequency
        for num, frequency in frequency_Dict.items():
            # Stop if we have filled the nums array to its original length
            if actual_Index == len(nums):
                break
            
            # Place the unique number at the current index
            nums[actual_Index] = num
            actual_Index += 1  # Move to the next index for the next unique number

            # If the number has duplicates and there's space in nums
            if frequency > 1 and actual_Index < len(nums):
                # Place the number again for the second occurrence
                nums[actual_Index] = num
                actual_Index += 1  # Move to the next index

        # Return the number of elements that are now in the modified nums
        return actual_Index

# Time Complexity: O(n), where n is the number of elements in nums
# Space Complexity: O(n) for the frequency dictionary storing counts of unique elements