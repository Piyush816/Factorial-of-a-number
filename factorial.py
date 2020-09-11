def factorial(n):
    x = 1
    for i in range(1, int(n) + 1):
        x = x * i
    print("factorial of", n, "is", x)



while True:
    n = input("enter number to know there factorial or (q) to quit the program:  ")
    if n!="q":
        factorial(n)
    else:
        print("see you later")
        break








