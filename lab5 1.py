values=[10, 20, 30]

keys=["dziesiec", "dwadziescia", "trzydziesci"]
D=dict(zip(keys, values))
print(D)
#print(list(zip(keys, values)))


x=len(keys)
for i in range(x):
    D[keys[i]]=values[i]
print(D)