def climb_stairs(n):
n==1
return n
n==2
return n
prev1, prev2 = 2, 1

for(i in range(3, n+1):
    current=prev1+prev2
    prev1=prev2
    prev2=current
return current

print(climb_stairs(4))
