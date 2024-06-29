def fizz_buzz(n):
    for a in range(1, n+1):
        if a%3 == 0 and a%5 == 0:
            print("fizz_buzz")
        elif a%3 == 0:
            print("fizz")
        elif a%5 == 0:
            print("buzz")
        else:
             print(a)    
n = int(input("Ввести число:  "))
fizz_buzz(n)