a=int(input('1つ目の整数:'))
b=input('算術演算子:')
c=int(input('2つ目の整数:'))

match b:
    
    case "+":
        print(f'{a}{b}{c}={a+c}')
    
    case "-":
        print(f'{a}{b}{c}={a-c}')
    
    case "*":
        print(f'{a}{b}{c}={a*c}')

    case "/":
        print(f'{a}{b}{c}={a//c}')
    
    case "%":
        print(f'{a}{b}{c}={a%c}')

    case _:
        print('エラー')  