N,Q,Limit=map(int,input().split())
weight=list(map(int,input().split()))
priority=list(map(int,input().split()))

weight.sort()
boat_count=0

heavy=len(weight)-1
light=0

while light<=heavy:
    if weight[heavy]+weight[light]<=Limit and not (priority[light]==1 and priority[heavy]==1):
        pair="yes"
        heavy-=1
        light+=1
    else:
        heavy-=1
        pair="no"
    boat_count+=1



print("Minimum boats required: ",boat_count)
for _ in range(Q):
    query=input().split()

    if query[0]=="CANPAIR":
        if (weight[query[1]] + weight[query[2]] <= Limit) and not (priority[query[2]] == 1 and priority[query[2]]==1):
            print("Yes")
        else:
            print("No")

    else:
        if query[1]<boat_count:
           rem= N-(2*int(query[1]))
           print("remaining people: ",rem)
        elif query[1]>=boat_count:
            print("everyone evacuated")




