s= "hi welcome to class"
print(s)
print(type(s))
s1=s.upper()
s_tit =s.title()
s2=s.capitalize()
s3=s.swapcase()
s4=s.casefold()
s5=s.lower()
s6=s.encode()

print(*(s1,s_tit,s2,s3,s4,s5,s6,),sep="\n")

e= "i am ushapujari7"
print(e.center(20,"#"))
print(e.rjust(30,"*"))
print(e.ljust(30,"*"))
print(e.zfill(25))
print(e.endswith("pujari7"))
print(e.startswith("pujari7"))
print(len(e))
#split method
sp= "i am going to office"
print(sp.split())
sp1 = "apple,banana,orange"
print(sp1.split(','))
#Find method
fn= "my name is usha, i am here to learn python"
print(fn.find("name"))
print(fn.find("Python"))
#isalpha
e1= "helloworld"
print(e1.isalpha())
#isalnum
e2= "9999999"
print(e2.isalnum())

e3="hi hello how are you usha"
cou=e3.count("h")
print(cou)

name = "usha"
age = 24
st = "My name is {} and I am {} years old.".format(name, age)
print(st)
#slicing
sl="my name is usha,i am from somandepalli"
print(sl[0])
print(sl[4:9])
print(sl[-6:])
print(sl[:15])

fruits = ["apple", "banana", "cherry"]
s4=fruits.append("orange")
print(s4, fruits)

def alphanum(input_string):

    if input_string.isalnum():
        print(f"'{input_string}' is alphanumeric.")
    else:
        print(f"'{input_string}' is not alphanumeric.")g

user_input = input("Enter a string: ")
alphanum(user_input)











