#for i in range(10):
#  print(i)

#for j in range(10,20):
#    print(j*2)

#for c in range(50,100,5):
#    print(c)


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



