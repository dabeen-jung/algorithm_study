'''
공과 잡초
'''

for tc in range(1,int(input())+1):
    s = input()

    result = 0
    i = 0
    while(i < len(s)):
        if s[i] == '(':
            if s[i+1] == ')':
                result += 1
                i += 1
            else:
                result += 1
        elif s[i] == ')':
            result += 1
        i += 1

    print('#%d %d'%(tc,result))