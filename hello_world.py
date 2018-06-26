test = [1,2,3,4,5,6,7,8,85,22,13,14]

filtered = [test[i] for i in range(len(test)) if test[i] % 2 == 0]

print(filtered)