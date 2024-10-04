from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_Index = actual_Index = 0  # Initialize indices for tracking positions in nums
        n = len(nums)  # Get the length of the input list

        # Loop until we have processed all elements in nums
        while current_Index < n:
            # Break if we've filled up to the original length
            if actual_Index == n:
                break
            
            # Place the current number at the actual index
            nums[actual_Index] = nums[current_Index]
            actual_Index += 1  # Move to the next position for unique numbers

            next_Index = current_Index + 1  # Check the next index for duplicates
            # If there's a duplicate and we have space in nums
            if (next_Index < n and 
                actual_Index < n and 
                nums[next_Index] == nums[current_Index]):
                nums[actual_Index] = nums[current_Index]  # Place the duplicate
                actual_Index += 1  # Move to the next position

            # Skip all duplicates of the current number
            while (next_Index < n and 
                   nums[next_Index] == nums[current_Index]):
                next_Index += 1  # Move to the next index
            
            current_Index = next_Index  # Update current_Index to the next unique number

        return actual_Index  # Return the count of unique elements

# Time Complexity: O(n), where n is the number of elements in nums
# Space Complexity: O(1), as we are modifying the list in place without using extra space