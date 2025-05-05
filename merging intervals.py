# given a list of intervals, return a final list with non overlapping intervals

# Input [[1,4], [2,7], [9,12]] must return [[1,7], [9,12]]

l= [[1,4], [2,7], [9,12]]

start= l[0][0]
current_end= l[0][1]

res= []

for i in range(1, len(l)):
  if (l[i][0] >= current_end):
    res.append([start, current_end])
    start= l[i][0]
    current_end= l[i][1]
  else:
    current_end= max(current_end, l[i][1])

res.append([start, current_end])

print(res)
