def ispalindromic(num):
    if str(num) == str(num)[::-1]:
        return True

def lychrel(num,count):
    if count == 50:
        return True
    else: 
        res = num+int(str(num)[::-1])
        if ispalindromic(res):
            return False
        else:
            count += 1
            return lychrel(res,count)

sum = 0

for i in range(10000):
    if lychrel(i,0):
        sum += 1

print(sum)
