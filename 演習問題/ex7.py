data = [int(x) for x in input("整数型データを入力してください。\n").split()]

max = data[0]
min = data[0]
for x in data:
    if max < x:
        max = x
for x in data:
    if min > x:
        min = x
print(f"最大値は{max}、最小値は{min}です。")
