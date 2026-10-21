a = [[5, 9, 1], [2, 3, 7]]
rows = len(a)
cols = len(a[0])
b = [[0]*rows for _ in range(cols)]
print(a)
for i in range(rows):
    for j in range(cols):
        b[j][i] = a[i][j]
print(b)
