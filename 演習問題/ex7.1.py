y = input("整数型データを入力してください。\n").split()
a = []
for x in y:
    a.append(int(x))
print(f"{a}")
print(type(a[1]))

max = a[0]
min = a[0]
for x in a:
    if max < x:
        max = x
for x in a:
    if min > x:
        min = x
print(f"最大値は{max}、最小値は{min}です。")
