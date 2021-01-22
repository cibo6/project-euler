def ispalindromic(num):
    if str(num) == str(num)[::-1] and \
    bin(num)[2:] == bin(num)[2:][::-1]:
        return True

sum = 0

for i in range(1000000):
    if ispalindromic(i):
        sum += i

print(sum)
