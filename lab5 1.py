values=[10, 20, 30]

keys=["dziesiec", "dwadziescia", "trzydziesci"]
D=dict(zip(keys, values))
print(D)
#print(list(zip(keys, values)))


x=len(keys)
for i in range(x):
    D[keys[i]]=values[i]
print(D)

D2 = dict(trzydziesci= 30, czterdziesci=40, piecdziesiat= 50)

D3 = D.copy()
D3.update(D2)
print(D3)
