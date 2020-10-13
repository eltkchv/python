def matrix():
    A = []
    print('enter elements\n')
    for i in range(3):
        A.append([])
        for j in range(3):
            A[i].append(int(input()))
    return (A)

def addition(A, B, R):
    for i in range(3):
        for j in range(3):
            R[i][j] = A[i][j] + B[i][j]
    for r in R:
        print(r)


def substraction(A, B, R):
    for i in range(3):
        for j in range(3):
            R[i][j] = A[i][j] - B[i][j]
    for r in R:
        print(r)


def multiplication(A, B, R):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                R[i][j] += A[i][k] * B[k][j]
    for r in R:
        print(r)


M1 = matrix()
print('M1:\n', M1)
M2 = matrix()
print('M2:\n', M2)

res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print('Сложение')
addition(M1, M2, res)
print('___________\n')
print('Вычитание')
substraction(M1, M2, res)
print('___________\n')
print('Умножение')
multiplication(M1, M2, res)