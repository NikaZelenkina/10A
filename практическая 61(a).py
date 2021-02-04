n=input("введите строку")
a=n.split()
s=0
for i in range(len(a)):
    if len(a[i])>s:
        s=len(a[i])
        s1=a[i]
print(s1,"длина",s)
