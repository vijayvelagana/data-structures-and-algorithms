

n = int(input("enter the value of n: "))

def n_total(n):
    # n(n+1)/2
    return int((n*(n+1)) / 2)
    
def n_squares_total(n):
    # n(n+1)(2n+1)/6
    return int((n*(n+1)*(2*n+1)) / 6)
    
def n_cube_total(n):
    return n_total(n) ** 2
    
print(f"n total: {n_total(n)}")
print(f"n total: {n_squares_total(n)}")
print(f"n total: {n_cube_total(n)}")
