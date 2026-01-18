subs=[set() for _ in range(N+1)]

messages=[]
msg_id=0
time=0

def broadcast(u,m):
    global msg_id,time
    msg_id+=1
    time+=1
    messages.append((msg_id,u,time,m%3==0))
def subscribe(u,v):
    subs[u].add(v)
def unsubscribe(u,v):
    subs[u].discard(v)
def fetch(u):
    feed=[]
    for mid,sender,t,critical in reversed(messages):
        if sender==u or sender in subs[u]:
            feed.append(mid)
            if len(feed)==10:
                break
    if feed:
        print(feed)
