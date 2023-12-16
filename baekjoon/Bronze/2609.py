#최대공약수와 최소공배수 (브론즈1)

a,b=map(int,input().split())

def gcd(a, b):
    if(a%b==0):
        return b
    return gcd(b,a%b)

def lcm(a,b,m):
    return m*(a//m)*(b//m)

print(gcd(a,b))
print(lcm(a,b,gcd(a,b)))
