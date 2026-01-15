N,Q,K=map(int,input().split())
temp=list(map(int,input().split()))

nextHot=[0]*N
stack=[]

for i in range(N):
    while stack and temp[i]>=temp[stack[-1]+K]:
        idx=stack.pop()
        nextHot[idx]=i

    stack.append(i)

    nextcold=[]
    stack.clear()
    for i in range(N):
        while stack and temp[i]<=temp[stack[-1]]-K:
            idx=stack.pop()
            nextcold[idx]=i
        stack.append(i)

    alert=[0]*N

    for i in range(N):
        if nextHot[i]!=0 and nextcold[i]!=0:
            alert[i]=min(nextHot[i],nextcold[i])
        else:
            alert[i]=max(nextHot[i],nextcold[i])

    pref=[0]*N
    pref[0]=1 if alert[0] !=0 else 0

    for i in range(1,N):
        pref[i]=pref[i-1]
        if alert[i]!=0:
            pref[i]+=1

for _ in range(Q):
    query=input().split()

    if query[0]=="NEXT":
        X=int(query[1])

        if alert[X]==0:
            print("No alert")
        else:
            print(alert[X])



    else:
        L=int(query[1])
        R = int(query[2])

        if L == 0:
            print(pref[R])
        else:
            print(pref[R] - pref[L - 1])
