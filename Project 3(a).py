def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))
S = input("Enter the number : ")
S = int(S)
result = factorial(S)
print("Factorial of",S,"is",result)