name=input("введите имя файла")
rash=input("ведите новое расширение")
def zamena(n,r):
    if n.count(".")>0:
        n=n[:n.rfind(".")+1]+r
    else:
        n=n+"."+r
    return n
print (zamena(name,rash))
