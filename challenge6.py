from collections import Counter
nums=input().split()

length=len(nums) #2n

num_count=Counter(nums)

len_of_identifier=length/2

for token in nums:
    if num_count[token]==len_of_identifier:
        print(token)
        break
    else:
        continue

