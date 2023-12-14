#방 번호 - 다시풀기

n = input()
arr = {'0':0, '1':0, '2':0, '3':0 , '4':0, '5':0,
       '7':0, '8':0}
cnt = 1
rep = 0

#오답
for v in n:
    if v == '6' or v=='9':
        rep+=1
        if rep >= 2:
            cnt+=1
            rep=1
        else:
            rep+=1
        continue
    if arr[v] < cnt:
        arr[v]+=1
    else:
        arr[v]+=1
        cnt+=1

print(cnt)

# 답
# 왜 둘의 갯수가 같은 경우에는 6의 배열 값을 올려주는거고,
# 다를 때는 9를 올려주는것인가
# n = int(input())
# card = [0] * 10
# for i in str(n):
#     if i == "9" or i == "6":
#         if card[6] == card[9]:
#             card[6] += 1
#         else:
#             card[9] += 1
#     else:
#         card[int(i)] += 1
# 
# print(max(card))