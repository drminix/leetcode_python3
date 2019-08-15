from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    """Given an array of integers, return indicies of the two numbers such that they add up to the target number"""
    #computational complexity: O(N) since we iterate through n elements only once
    #space comlexity: O(N) since we need to store n elements in the array

    #(0) use hashtable to store the number and its index.
    hashTable={}
    #(1) iterating through all the itmes
    for i in range(len(nums)):
        complement = target - nums[i]
        #(2) check if the complement is in the hashTable. If not, put it into the hashtable
        if complement in hashTable:
            return [hashTable[complement],i]
        else:
            hashTable[nums[i]] = i