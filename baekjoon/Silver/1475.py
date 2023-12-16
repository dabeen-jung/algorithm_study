#방 번호 - 실버5

n = input()
arr = {'0':0, '1':0, '2':0, '3':0 , '4':0, '5':0,'6':0 , '7':0, '8':0}


for v in n:
    if v == '6' or v=='9':
        arr['6']+=1
    else:
        arr[v] += 1

mok = arr['6'] // 2
if arr['6'] % 2 ==1:
    arr['6'] = mok +1
else:
    arr['6'] = mok


print(max(arr.values()))
