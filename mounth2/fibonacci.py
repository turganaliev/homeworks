n = int(input('Enter a number: '))
def fibbo(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbo(n - 1) + fibbo(n - 2)

fibbo_list = []
for i in range(n):
    a = fibbo(n - 1)
    fibbo_list.append(a)
    n -= 1

fibbo_list.reverse()
print(fibbo_list)