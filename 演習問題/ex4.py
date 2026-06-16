data=float(input("データ:"))
if data==0:
    print("データなし")

else:
    count=0
    sum=0
    
    while data!=0:
        sum+=data
        count+=1
        data=float(input("次のデータ:"))

    
    print(f"件数:{count}")
    print(f"合計{sum}")
    print(f"平均{sum/count}")