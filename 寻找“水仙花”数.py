def three(n):
    return n*n*n
for i in range(100,999):
    i_b = int(i / 100)
    i_s = int((i % 100) / 10)
    i_g = int(i % 10)
    if three(i_g)+three(i_s)+three(i_b) == i:
print(i)
