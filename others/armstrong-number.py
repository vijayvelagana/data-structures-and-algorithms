

num = int(input("Enter a number to validate Armstrong number: "))

count = 0
num_copy = num

if num_copy < 0:
    print(False)
    
while num_copy > 0:
    last_digit = num_copy % 10
    count += 1
    num_copy = num_copy // 10
    
result = 0
num_copy = num
while num_copy > 0:
    last_digit = num_copy % 10
    result += pow(last_digit, count)
    num_copy //= 10
    
print(result)
print(num == result)
