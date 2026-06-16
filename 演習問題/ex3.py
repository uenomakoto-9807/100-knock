n=int(input("自然数n="))

if n<=0 or n>=200:
    print("入力エラー")

else:
    
    sum=n
    for i in range (1,n):
        sum+=i
        
    print(f"1から{n}までの和は{sum}です。")