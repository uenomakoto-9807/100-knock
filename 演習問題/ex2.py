a=int(input('1つ目の整数:'))
b=input('算術演算子:')
c=int(input('2つ目の整数:'))
if b=="+":
    print(f'{a}{b}{c}={a+c}')
    
elif b=="-":
    print(f'{a}{b}{c}={a-c}')
    
elif b=="*":
    print(f'{a}{b}{c}={a*c}')

elif b=="/":
    print(f'{a}{b}{c}={a//c}')
    
elif b=="%":
    print(f'{a}{b}{c}={a%c}')

else:
    print('エラー')  