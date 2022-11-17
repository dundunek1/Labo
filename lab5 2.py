sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

for i in sample_dict.keys():
 print(i,sample_dict[i])

for k, v in sample_dict.items():
 print(f'{k:<8} = {v:>8}')

#d2={}
l = ["name", "age", "city", "a"]
#for i in l:
 #if i in sample_dict.keys():
    #d2[i]=sample_dict[i]
d2={k:sample_dict[k] for k in l if k in sample_dict.keys()}
print(d2)

d3= sample_dict.copy()

for i in l:
 if i in d3:
  d3.pop(i)
print(d3)

d3 = sample_dict.copy()
for i in l:
    if i in d3:
        d3.pop(i)
print(d3)
od Jakub Słowik w68565 do każdy:    3:04 PM
sample_dict["locatiob"] = sample_dict["city"]
del sample_dict["city"]