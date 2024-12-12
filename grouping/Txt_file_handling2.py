#open() have filename, and mode.
demo=open('Sample_test')
data=demo.readline()
demo.tell()
data2=demo.readline()
demo.seek(100)
remaining=demo.read()
print('line1:' ,data)
print('line2:' ,data2)
print('rem:' ,remaining)
print(demo.tell())

print(f"data {data}")
print(f"data2 {data2}")
print(f"remaining {remaining}")

with open("sample_test", "r") as file:
    print("First 5 Characters:", file.read(5))
    file.seek(0)
    print("Remaining:")
    print(file.read())

#readlines

with open("Sample_test", "r") as file:
    print("\nUsing readlines():")
    print(file.readlines())

with open("Sample_test", "r") as file:
    lines = file.readlines(20)
    print("Lines:")
    print(lines)


