#STRINGS
#Write a Python program to count the number of vowels in a given string
s="Welcome to Python World"
vowels=['a','e','i','o','u']
count=0
for i in s:
    if i.lower() in vowels:
        count+=1
print(count)

#Reverse the string "Python is fun!" without using slicing.
r="Python is fun"
r1=""
for i in r:
    r1=i+r1
print(r1)

#Check if the string "madam" is a palindrome.

string = "madam"
if string== string[::-1]:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')

#Find and replace the word "Python" with "Programming" in the string "I love Python."
s= "I love Python."
s1 = s.replace("Python", "Programming")
print(s1)

#Convert the string "hello world" to the title case.
s= "hello world"
tit= s.title()
print(s)

#Extract all the digits from the string "abc123xyz456".
import re
s2 = "abc123xyz456"
digits = re.findall(r'\d+', s2)
result = ''.join(digits)

print(result)

#Join a list of strings ["Python", "is", "awesome"] into a single string separated by spaces.
s5 = ["Python", "is", "awesome"]
word= ' '.join(s5)
print(word)

#Write a Python program to check if a given string starts with "Hello".
s = "Hello, world!"
if s.startswith("Hello"):
    print(f'The string starts with "Hello".')
else:
    print(f'The string does not start with "Hello".')

#Count the occurrence of each character in the string "hello".
s = "hello"
char_count = {}
for i in s:
    char_count[s] = char_count.get(s, 0) + 1
print(char_count)

#Split the string "apple, banana, cherry" by commas.
s = "apple, banana, cherry"
fruits = s.split(", ")
print(fruits)



