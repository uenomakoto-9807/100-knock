def pfact(n):
    print(f"素因数分解:{n}=", end="")
    x = 2
    while n % x != 0:
        x += 1
    print(f"{x}", end="")
    n //= x
    while n % 2 == 0:
        print(f"*{2}", end="")
        n //= 2

    f = 3
    while f * f <= n:
        if n % f == 0:
            print(f"*{n}", end="")
            n //= f
        else:
            f += 2
    if n != 1:
        print(f"*{n}", end="")


a = int(input("正の整数:"))
if a < 2:
    a = int(input("正の整数:"))
pfact(a)
