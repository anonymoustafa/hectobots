x = [1, 1] # this is an array
for i in range(2, 10): 
    x.append(x[-1] + x[-2])
print(', '.join(str(y) for y in x))