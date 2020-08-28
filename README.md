# CS Build Week 2: Interview Prep
---
## [https://leetcode.com/problems/contains-duplicate/]  📗easy  
> Given an array of integers, find if the array contains any duplicates.
> 
> Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.  
> 
> **Example 1:**
>> ```python 
>> Input: [1,2,3,1]  
>> Output: true  
>> ```
> 
> **Example 2:**
>> ```python
>> Input: [1,2,3,4]
>> Output: false
> 
> **Example 3:**
>> ```python
>> Input: [1,1,1,3,3,4,3,2,4,2]
>> Output: true
>> ```
>
## [https://leetcode.com/problems/add-two-numbers/]  📙medium  
> You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
> 
> You may assume the two numbers do not contain any leading zero, except the number 0 itself.
> 
> **Example:**
>> ```python 
>> Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)  
>> Output: 7 -> 0 -> 8  
>> Explanation: 342 + 465 = 807.  
>> ```
>
## [https://leetcode.com/problems/two-sum/]  📗easy  
> Given an array of integers `nums` and and integer `target`, return *the indices of the two numbers such that they add up to `target`.*
> 
> You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.
> 
> You can return the answer in any order.
> 
> **Example 1:**
>> ```python 
>> Input: nums = [2,7,11,15], target = 9  
>> Output: [0,1]  
>> Output: Because nums[0] + nums[1] == 9, we return [0, 1]  
>> ```
> 
> **Example 2:**
>> ```python
>> Input: nums = [3,2,4], target = 6
>> Output: [1,2]
> 
> **Example 3:**
>> ```python
>> Input: nums = [3,3], target = 6
>> Output: [0,1]
>> ``` 
> 
> **Constraints:**
>> 
>> - `1 <= nums.length <= 105`
>> - `-109 <= nums[i] <= 109`
>> - `-109 <= target <= 109`
>> - **Only one valid answer exists.**
>
## [https://leetcode.com/problems/implement-queue-using-stacks/]  📗easy  
> Implement the following operations of a queue using stacks.
> 
>> - push(x) -- Push element x to the back of queue.  
>> - pop() -- Removes the element from in front of queue.  
>> - peek() -- Get the front element.  
>> - empty() -- Return whether the queue is empty.  
> 
> **Example:**  
> ```python 
> MyQueue queue = new MyQueue();  
> 
> queue.push(1);  
> queue.push(2);  
> queue.peek();  // returns 1  
> queue.pop();   // returns 1  
> queue.empty(); // returns false  
> ```
> 
> **Notes:**  
>> You must use *only* standard operations of a stack -- which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
>>Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
>> You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
>
## [https://leetcode.com/problems/merge-two-sorted-lists/]  📗easy  
> Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
> 
> **Example:**
>> ```python
>> Input: 1->2->4, 1->3->4  
>> Output: 1->1->2->3->4->4  
>> ```
>
## [https://leetcode.com/problems/decode-string/]  📙medium  
> Given an encoded string, return its decoded string.
> 
> The encoding rule is: `k[encoded_string]`, where the *encoded_string* inside the square brackets is being repeated exactly *k* times. Note that *k* is guaranteed to be a positive integer.
>  
> You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
> 
> Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, *k*. For example, there won't be input like `3a` or `2[4]`.
> 
> **Example 1:**
>> ```python 
>> Input: s = "3[a]2[bc]"  
>> Output: "aaabcbc"  
>>
> **Example 2:**
>> ```python
>> Input: s = "3[a2[c]]"
>> Output: "accaccacc"
>> ```
> 
> **Example 3:**
>> ```python
>> Input: s = "2[abc]3[cd]ef"
>> Output: "abcabccdcdcdef"
>> ```
> 
>  **Example 4:**
>> ```python
>> Input: s = "abc3[cd]xyz"
>> Output: "abccdcdcdxyz"
>> ```
>
## [https://leetcode.com/problems/find-the-duplicate-number/]  📙medium  
> Given an array *nums* containing *n* + 1 integers where each integer is between 1 and *n* (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
> 
> **Example 1:**
>> ```python
>> Input: [1,3,4,2,2]  
>> Output: 2  
>> ```
> 
> **Example 2:**
>> ```python  
>> Input: [3,1,3,4,2]  
>> Output: 3  
>> ```  
> 
> **Note:**
> 
>> 1. You **must not** modify the array (assume the array is read only).
>> 1. You must use only constant, *O(1)* extra space.
>> 1. Your runtime complexity should be less than *O(n2)*.
>> 1. There is only one duplicate number in the array, but it could be repeated more than once.  
>  
  
## [https://leetcode.com/problems/search-in-rotated-sorted-array/]  📙medium  
> Given an integer array `nums` sorted in ascending order, and an integer `target`.
> 
> Suppose that `nums` is rotated at some pivot unknown to you beforehand (i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).
> 
> You should search for target in `nums` and if you found return its index, otherwise return -1.
> 
> **Example 1:**
>> ```python
>> Input: nums = [4,5,6,7,0,1,2], target = 0  
>> Output: 4  
>> ```
> 
> **Example 2:**
>> ```python
>> Input: nums = [4,5,6,7,0,1,2], target = 3
>> Output: -1  
>> ```
>
> **Example 3:**
>> ```python
>> Input: nums = [1], target = 0  
>> Output: -1  
>> ```
> 
> **Constraints:**  
> 
>> - `1 <= nums.length <= 5000`  
>> - `-10^4 <= nums[i] <= 10^4`  
>> - All values of `nums` are **unique**.  
>> - `nums` is guranteed to be rotated at some pivot.  
>> - `-10^4 <= target <= 10^4`  
