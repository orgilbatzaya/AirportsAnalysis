'''
Created on Dec 11, 2017

@author: orgil
'''
import operator
import re
def selection(nums):
    for i in range(len(nums)):
        small = min(nums[i:])
        smallind = nums[i:].index(small)
        nums[i+smallind] = nums[i]
        nums[i] = small
    return nums
def bubble(nums):
    for i in range(len(nums)):
        for x in range(i):
            if nums[x]>nums[x+1]:
                temp = nums[x]
                nums[x] = nums[x+1]
                nums[x+1] = temp
    return nums
def mergesort(data):
    n = len(data)
    if n == 1:
        return data
    else:
        d1 = mergesort(data[:n/2])
        d2 = mergesort(data[n/2:])
        #return merge(d1, d2)
        
def mos(cars):
    oc = max([cars.count(w) for w in set(cars)])
    return sorted([i for i in set(cars) if cars.count(i) == oc])[0]
def most(cars):
    dict={}
    for car in cars:
        if car not in dict.keys():
            dict[car]=0
        dict[car] += 1
   
    sortedPairs=sorted(dict.items(), key=operator.itemgetter(0))    #Sorting alphabetical first...    
    sortedPairs=sorted(sortedPairs, key=operator.itemgetter(1), reverse=True)  #..then on the number of cars. 
    return sortedPairs[0][0]


'''phrasepsplit looks at n chars in phrase, takes about n steps'''
def split(phrase):
    ans = []
    pos = 0
    st = 0
    for x in range(len(phrase)):
        if not phrase[x].isalpha():
            pos = x
            ans.append(phrase[st:pos])
            st = pos
            
    return ans
def process(nums):
    if len(nums) > 0:
        process(nums[1:])
        print nums[0]     
if __name__ == '__main__':
    ans = []    
    a  = ["apple","cat",'1','12']
    a[2:] = [int(x) for x in a[2:]]
    ans.append(a)
    nums = [6,4,2,1,5]
    print process(nums)
    print type(a[2])
    
    
    
    
    data = [ ['Google', '21023', 65000, 5000, 3000],
['Two Sigma', '26853', 70000],
['Paypal', '21023', 60000, 10000],
['Capital One','26489', 55000, 5000, 4000],
['Google', '28311', 62000, 5000, 2000]]

    ans = []
    for i in data:
        if i[0] == "Google":
            ans.append((i[1],sum(i[2:])))
    ans = sorted(ans,key=operator.itemgetter(1))
    print ans
    a = [3,4,3,7]

    print 'ajn'.isalpha()
   
    
    
    
    
    