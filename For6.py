n=int(input())
s1=s2=s3=s4=s5=0; s6=3
for i in range(1,n+1):
    s1=i+s1
    a=1
    for k in range(1,i+1):
        a=a*k
    s3=a+s3
    a=i
    if i!=1:
        s2=(i-1)*i+s2
        z=0
        while a!=0:
            a=a//10
            z+=1
        s6=2*(10**z)+i+s6
    s4=i*10+2+s4
    s5=i/(i+1)+s5
print(s1,s2,s3,s4,s5,s6)