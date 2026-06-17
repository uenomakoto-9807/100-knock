def gcd(a,b,c):
    
    n=a
    while a%n!=0 or b%n!=0 or c%n!=0:
        n-=1
    return n
        
def lcm (a,b,c):
    t=a
    while t%a!=0 or t%b!=0 or t%c!=0:
        t+=1
    return t
    
x=int(input("1つ目の正の整数:"))
y=int(input("2つ目の正の整数:"))
z=int(input("3つ目の正の整数:"))
q=gcd(x,y,z)
e=lcm(x,y,z)
print(f"最大公約数は{q},最小公倍数は{e}です。")