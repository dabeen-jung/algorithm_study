'''
[그리디] ATM (실4)
'''

n = int(input())
bank = list(map(int,input().split()))

bank.sort() # [1 2 3 3 4]
time = 0
total = 0
for t in bank:
    time += t # 1 ->1, 1+2 ->3  total = 1+3=4
    total += time

print(total)