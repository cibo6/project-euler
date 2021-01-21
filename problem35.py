import math

res = 0

def isprime(num):
    if all(num%i != 0 for i in range(2,int(math.sqrt(num))+1)):
        return True
    else: return False

def rotate(n):
    return [n[i:]+n[:i] for i in range(len(n))]

for num in range(3,1000000,2):
    if all(num%i != 0 for i in range(2,int(math.sqrt(num))+1)):
        perms = list(rotate(str(num)))
        val = []
        for j in range(len(perms)):
            val.append(int("".join(perms[j])))
        #remove checking duplicates
        if all(isprime(val[k]) for k in range(len(val))):
            res += 1

print(res+1)
