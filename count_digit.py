n = 45678
num = n
count = 0   # initialize

while num > 0:
    count += 1
    num = num // 10

print(count)