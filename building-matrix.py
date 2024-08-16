def prnt(elements):
    print(' '.join(map(str, elements)))

def genMatrix(matrix, rows, cols):
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    for x, y, m in matrix:
        grid[x][y] = m
    return grid

# solution 1:

def build1(x, y):
    blocks = ['b', 'r', 'g']
    matrix = []
    size = x*y

    for i in range(x):
        for j in range(y):
            matrix.append([i, j, blocks[0]])
    for m in matrix:
        prnt(m)

    for l in range(size):
        if l != (size) - 1 :
            matrix[l][2]= 'x'
            prnt(matrix[l])
            matrix[l][2] = blocks[1]
        prnt(matrix[l])

    for l in range(size):
        if l != 0 :
            matrix[l][2]= 'x'
            prnt(matrix[l])
            matrix[l][2] = blocks[2]
        prnt(matrix[l])
    print('--')
    for row in genMatrix(matrix, x, y):
            print(' '.join(row))

# solution 2:

def build2(m, n):
    if m > 3 and n > 3:
        x = 0
        y = 0
        x1 = 1
        matrix = []

        while y < n-1:
            if y == 0:
                while x < m:
                    matrix.append([x, y, 'b'])
                    x += 2
            else:
                while x1 < m:
                    matrix.append([x1, y, 'b'])
                    x1 += 2
            y += 2

        if m%2 != 0 and n%2 != 0:
            l = m-2
            o = n-2
        else:
            l = m-1
            o = n-1

        y = 1
        while y <= o:
            x = 1 
            while x <= l:
                matrix.append([x, y, 'r'])
                x += 2
            y += 2
        
        y = 2
        while y <= o:
            x = 2
            while x <= l:
                matrix.append([x, y, 'r'])
                x += 2
            y += 2

        for mat in matrix:
            if mat[2] == 'b':
                matrix.append([mat[0], mat[1], 'x'])

        for mat in matrix:
            if mat[2] == 'b':
                matrix.append([mat[0], mat[1], 'g'])

        for i in range(m):
            for j in range(n):
                if [i, j, 'r'] not in matrix:
                    matrix.append([i, j, 'g'])

        reds = []
        for mat in matrix:
            if mat[2] == 'r':
                reds.append(mat)
        
        for mat in matrix:
            prnt(mat)
        print('--')
        for row in genMatrix(matrix, m, n):
            print(' '.join(row))

build2(6,7)
