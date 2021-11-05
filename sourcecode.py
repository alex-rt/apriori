T = [['A', 'C', 'D'],
    ['B', 'C', 'E'],
  ['A', 'B', 'C', 'E'],
  ['B', 'E']]

C=[['A','B','C','D','E'][['A','B'],['A','C'],['A','E'],['B','C'],['B','E'],['C','E']],
['B','C','E']]
L=[[],[],[],[]]
min_sup = 2
count = 0
k=0

for i in T:
  for i in i:
    print(i)

def countOccurrences(my_list, term):
  counts = {}
  
  for row in my_list:
    if row[term] not in counts:
      counts[row[term]] = 0
    counts[term] += 1
  return counts

while k>3:
  for item in T:
    if item in C[k] == True:
      C[k].append(item)
      k=k+1

k2=0
while k2>3:
  for candidate in C:
    ocurrences = countOcurrences(C, candidate)
    if ocurrences> min_sup:
      L[k2].append(candidate)
      
min_sup = 2




