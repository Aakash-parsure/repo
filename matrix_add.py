X = [ [1,2,3],
      [4,5,6],
      [7,8,9] ]

Y = [ [10,11,12],
      [13,14,15],
      [16,17,18] ]

Result = [ [0,0,0],[0,0,0],[0,0,0]]

#print(len(X)) -- 3
#print(len(X[0])) -- 3

for i in range(len(X)):
    for j in range(len(X[0])):
        Result[i][j] = X[i][j] + Y[i][j]

for r in Result:
    print(r)
