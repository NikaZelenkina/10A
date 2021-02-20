def TumbaWorlds(A,w,L):
    if len(w)==L:
        if w[1]=="Ы":
            print(w)
        return
    for c in A:
        TumbaWorlds(A,w+c,L)
k=int(input())   
TumbaWorlds("ЫШЧО","",k)
