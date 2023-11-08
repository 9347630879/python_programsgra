
for i in range(0,5):
    for j in range(0,i + 1):
        print("1",end='')
    print("\r")


def pattern(n):
    for i in range(1,n + 1):
        for j in range(1,i + 1):
            print(j,end=" ")
        print()
rows = 10
pattern(rows)
