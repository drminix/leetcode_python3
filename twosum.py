 def twoSum(self, nums: List[int], target: int) -> List[int]:
    """Given an array of integers, return indicies of the two numbers such that they add up to the target number"""
    #(0) use hashtable to store the number and its index.
    #Computational complexity O(N) since we iterate through n elements only once
    hashTable={}
    #(1) iterating through all the itmes
    for i in range(len(nums)):
        complement = target - nums[i]
        #(2) check if the complement is in the hashTable. If not, put it into the hashtable
        if complement in hashTable:
            return [hashTable[complement],i]
        else:
            hashTable[nums[i]] = i