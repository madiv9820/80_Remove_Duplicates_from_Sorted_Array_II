# 80. Remove Duplicates from Sorted Array II

__Type:__ Medium <br>
__Topics:__ Array, Two Pointers <br>
__Companies:__ Microsoft, Bloomberg, Amazon, Google, tcs, Adobe, Apple, Yahoo, TikTok, Zoho, Uber, Yandex <br>
__LeetCode Link:__ [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
<hr>

### Question

Given an integer array `nums` sorted in __non-decreasing order__, remove some duplicates [__in-place__](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears __at most twice__. The __relative order__ of the elements should be kept the __same__.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the __first part__ of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` _after placing the final result in the first_ `k` _slots of_ `nums`.

Do __not__ allocate extra space for another array. You must do this by __modifying the input array__ [__in-place__](https://en.wikipedia.org/wiki/In-place_algorithm) with O(1) extra memory.

__Custom Judge:__

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be __accepted__.
<hr>

### Examples

__Example 1:__ <br>

__Input:__ nums = [1,1,1,2,2,3] <br>
__Output:__ 5, nums = [1,1,2,2,3,_] <br>
__Explanation:__ Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. <br>
It does not matter what you leave beyond the returned k (hence they are underscores).

__Example 2:__

__Input:__ nums = [0,0,1,1,1,1,2,3,3] <br>
__Output:__ 7, nums = [0,0,1,1,2,3,3,_,_] <br>
__Explanation:__ Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively. <br>
It does not matter what you leave beyond the returned k (hence they are underscores).
<hr>

### Constraints:

- <code>1 <= nums.length <= 3 * 10<sup>4</sup></code>
- <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
- `nums` is sorted in __non-decreasing__ order.
