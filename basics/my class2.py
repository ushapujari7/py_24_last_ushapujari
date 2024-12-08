li= [1, 2, 3,9.0,6.5,2+3j,"usha","venky",True,False]
#Slicing an element from list
print(li[0])
print(li[5])
sl_li= li[1:4]
print(sl_li)
print(li[2::6])
print(li[:6])
print(li[5:])
print(li[-5:-1])

#add an element from list
li.append(4)
print(li)
#Remove an element from list
li.remove(3)
print(li)
#sorting an element from list
li1 = [5, 3, 8, 6, 7, 2, 10]
li1.sort()
print(li1)
# comprehension
li_com = [5, 3, 8, 6, 7, 2, 10]
square = [x**2 for x in li_com]
mod = [x%2 for x in li_com]
add = [x+2 for x in li_com]
print(square)
print(mod)
print(add)
# intersecting an element in list
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
l_intersect = [value for value in list1 if value in list2]
print(l_intersect)
# remove duplicate
li_du= [9,4,7,6,3,3,2,2,8,9,5,4]
li6 = list(set(li_du))
print(li6)
print(max(li6))
print(min(li6))


def list_1():
    names = ["usha","venky","nithin","purnesh","kiran"]
    print(names)
    print("\n:")
    print(f"First element: {names[0]}")
    print(f"Last element: {names[-1]}")
    names[1] = "rani"
    print("\n:",names )
    names.append("varun")
    print("\n:", names)
    names.insert(2, "nikhil")
    print("\n:", names)
    names.remove("nikhil")  #
    print("\n:", names)
    names.sort()
    print("\nS:", names)
    names.reverse()
    print("\n:", names)
    s9 = names[1:3]
    print("\n:", s9)
    if "venky" in names:
        print("\n'venky' is in the list!")
    else:
        print("\n'venky' is not in the list!")


(list_1())


