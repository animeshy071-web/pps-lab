n = int(input("dimension: "))

print("first matrix:")
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("second matrix:")
B = []
for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

# Initialize result matrix
result = [[0 for _ in range(n)] for _ in range(n)]

# Matrix multiplication
for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += A[i][k] * B[k][j]

print("Resultant Matrix:")
for row in result:
    print(*row)