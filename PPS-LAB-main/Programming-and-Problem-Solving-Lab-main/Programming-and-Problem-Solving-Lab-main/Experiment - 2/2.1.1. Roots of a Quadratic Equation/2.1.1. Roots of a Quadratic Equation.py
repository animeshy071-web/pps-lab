a, b, c = map(int, input().split())

D = b*b - 4*a*c

if D > 0:
    sqrt_D = D ** 0.5
    root1 = (-b + sqrt_D) / (2 * a)
    root2 = (-b - sqrt_D) / (2 * a)
    print(f"root1 = {root1:.2f}")
    print(f"root2 = {root2:.2f}")

elif D == 0:
    root = -b / (2 * a)
    print(f"root1 = root2 = {root:.2f}")

else:
    real_part = -b / (2 * a)
    imaginary_part = ((-D) ** 0.5) / (2 * a)
    print(f"root1 = {real_part:.2f}+{imaginary_part:.2f}i")
    print(f"root2 = {real_part:.2f}-{imaginary_part:.2f}i")

