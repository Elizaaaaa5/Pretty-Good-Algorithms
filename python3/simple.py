Link to the solution contributor page 
https://stackoverflow.com/questions/50743582/two-sum-python-solution

problem definition:
'''
  Given an array of integers, return indices of the two numbers such that they add up to a specific target.

  You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
  

Example:
'''
  Given nums = [2, 7, 11, 15], target = 9,

  Because nums[0] + nums[1] = 2 + 7 = 9,
  return [0, 1].
'''

#########################################################################################################################################
'''
num1bits
Write a function that takes an unsigned integer and returns the number of 1 bits it has.
'''
import numpy as np
def num1bits(num):
    b_num=bin(num)[2:]
    lst = [int(i) for i in str(b_num)]
    lst=np.array(lst)
    count=0
    for i in range(len(lst)):
        if lst[i]==1:
            count=count+1
    return count
