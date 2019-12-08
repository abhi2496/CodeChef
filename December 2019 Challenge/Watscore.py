#CodeChef Problem WATSCORE
try:
    t = int(input())
    res={}
    scores=[]
    if t>0 and t<11:
        for iteration in range(t):
            total=0
            n = int(input())
            if n>0 and n<1001:
                for i in range(n):
                    p,s=list(map(int,input().split()))
                    if (p>0 and p<12) and (s>=0 and s<101):
                        if p in res.keys():
                            if int(s)>int(res[p]):
                                res[p]=s
                        else:
                            res.update({p:s})
            for key in res.keys():
                if int(key)<9:
                    total+=int(res[key])
            scores.append(total)
            res.clear()
    
    for score in scores:
        print(score)

except Exception as e:
    pass
