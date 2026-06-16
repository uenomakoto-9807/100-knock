test=int(input('成績:'))
if test < 0 or test > 100:
     print('入力エラーです。')

elif test>=80:
    print(f'{test}点は優です。')
elif test>=70:
    print(f'{test}点は良です。')
elif test>=60:
    print(f'{test}点は可です。')
else:
    print(f'{test}点は不可です。')