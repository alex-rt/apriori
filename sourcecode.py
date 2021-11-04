T = [{'a','c','d'},{'b','c','e'},{'a','b','c','e'},{'b','e'}]
print(T)
C1= [{'a'},{'b'},{'c'},{'d'},{'e'}]
Lk = []
min_sup = 2
count = 0
for i in T:
  for i in i:
    print(i)

for i in T:
  for i in i:
    if {"i"} in C1 == True:
      count = count +1
    else:
      C1.append({i})

print(count)
print(C1)
