

num = int(input("Enter the value of num: "))
sqrt_num = int(num ** 0.5)
res = set()

for i in range(1, sqrt_num+1):
    if num % i == 0:
        res.add(i)
        res.add(int(num/i))
        
print(f"res: {res}")

# TC: O(sqrt(n))
# SC: O(f) ; f = number of factors


# ======================



num = int(input("Enter the value of num: "))

sqrt_num = int(num ** 0.5)

res = list()
for i in range(1, sqrt_num+1):
    if num % i == 0:
        res.append(i)
        if int(num/i) != i:
            res.append(int(num/i))
            
print(f"res: {res}")

# TC: O(sqrt(N))
# SC: O(F)

