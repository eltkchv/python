def matrix():
    A = []
    print('введите элементы\n')
    for i in range(n):
        A.append([])
        for j in range(m):
            A[i].append(int(input()))
    return (A)

def addition(A, B, R):
    for i in range(n):
        for j in range(m):
            print( A[i][j] + B[i][j], end = " ")
        print('\n')



def substraction(A, B, R):
    for i in range(n):
        for j in range(m):
            print(A[i][j] - B[i][j],end=" ")
        print('\n')


def multiplication(A, B, R):
    for i in range(n):
        for j in range(m):
            print(A[i][j] * B[i][j],end=" ")
        print('\n')

print ('введите количество строк')
n=int(input())
print ('введите количество столбцов')
m=int(input())
M1 = matrix()
print('M1:\n', M1)
M2 = matrix()
print('M2:\n', M2)

res = []

print('Сложение')
addition(M1, M2,res)
print('___________\n')
print('Вычитание')
substraction(M1, M2, res)
print('___________\n')
print('Умножение')
multiplication(M1, M2, res)