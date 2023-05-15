result = []
N = int(input())
a=1
while a<=N-2:
    b=a+1
    while b<=N-1:
        c = (a**2+b**2)**(0.5)
        if c == int(c) and a+b+c <= N:
            result.append(a+b+int(c)) 
        b+=1
    a+=1
    
cnt = 0
for i in range(0,len(result)):
    if result.count(result[i]) == 1:
        cnt+=1

print(cnt)
