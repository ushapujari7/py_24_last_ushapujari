def practice_1():
    for i in range(20):
        print(i+2)

def practice_2():
    for j in range(1,10):
        print(j*2)

def practice_3():
    for c in range(10,20,2):
        print(c)

def games(given_name):
    if "venkat"== given_name:
        print("given name ok")
    else:
        print("given name is not ok")


def multiples(x):
    for i in range(1,11):
        print(f'{x}*{i}={x*i}')

x= int(input("multiply with: "))

multiples(x)
games(input("guess name: "))  #calling function


practice_1()
practice_2()
practice_3()