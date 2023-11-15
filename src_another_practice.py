
#  recurise function

lst = []
def fib(n,a,b,i):
    if i<=n:
        lst.append(b)
        a = a + b
        b = a - b
        i = i + 1
        fib(n,a,b,i)
    else:
        print(lst)
fib(n = 10,a = 1, b = 0 , i  = 1)


# number patterns

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
r = 5
pattern(r)

# star pattern
i = int(input("enter a number of rows : "))
for j  in range(1,i+1):
    print("*"*j)


n = int(input("enter a number of rows : "))
for i in range(n):
    for j in range(n-i-1):
        print("",end="")
    for j in range(i+1):
        print("*",end="")
    print()


# inverted half pymarid

n = int(input("enter a number of rows : "))
for i in range(0,n):
    for j in range(1,n-i):
        print(j,end="")
    print()

# inverted pymarid number
n = int(input("enter a number of rows : "))
for i in range(n):
    for j in range(i,0,-1):
        print(j,end="")
    print()
