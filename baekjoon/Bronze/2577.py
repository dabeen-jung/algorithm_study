#숫자의 개수 (브론즈2)

res = 1
arr= {0:0, 1:0, 2:0,3:0, 4:0, 5:0 , 6:0, 7:0, 8:0, 9:0}

for i in range(3):
    res*=int(input())

ans=str(res)

for i in ans:
    arr[int(i)]+=1

for val in arr.values():
    print(val)
