def bank(a,time):
    for each_year in range(time):
       a += (a * 0.1)
    return a
 
a=float(input("Какая сумма? ")) 
time=int(input("Какой срок вклада? "))
print(bank(a, time))