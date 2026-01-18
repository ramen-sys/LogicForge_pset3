s=input().lower()
p=input().lower()
k=len(p)

from collections import Counter

p_count=Counter(p)
index=[]
for i in range(len(s)-k+1):
    window=s[i:i+k]
    window_count=Counter(window)
    if window_count==p_count:
        index.append(i)

    else:
        window_count.clear()
print(index)
