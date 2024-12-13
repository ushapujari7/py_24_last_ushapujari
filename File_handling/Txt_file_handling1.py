#data=open('Test1.txt' ,"r")
#print(data.read())

def read_file(file ,mode):
    try:
        with open(file ,mode) as data:
            return data.read()
    except ValueError:
        return f'this is read mode only but you are given {mode}'
    except FileNotFoundError:
        return f'file not exist'

result= read_file('Test1.txt' ,"r")
print(result)

def read_lines(file ,mode):
    try:
        with open(file ,mode) as data:
            return data.readlines()
    except ValueError:
        return f'this is read mode only but you are given {mode}'
    except FileNotFoundError:
        return f'file not exist'
    except Exception as e:
        return f"file error {e}"


result= read_lines('Test2.txt' ,"r")
print(result)
for i in result:
    print(i)

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Content successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = "example_write.txt"
content = "this is python class"

write_file(filename, content)

with open(filename, 'r') as file:
    print("\nContent of the file:")
    print(file.read())


def file_append(filename, add):
    try:
        with open(filename ,'a') as file:
            file.write(add)
            print(f"file is added succesfully to {filename}")
    except Exception as e:
        print(f"An error accured : {e}")

filename="Test3.txt"
add="\nThis is practice of appending data to file."
file_append(filename,add)
print(open("Test3.txt" ,"r").read())


answer=file_append('Test3.txt' ,'a')


def read_and_write_file(filename, content):
    try:
        with open(filename, 'r+') as file:
            print("Original Content of the File:")
            data1 = file.read()
            print(data1)
            file.write(content)
            print("\nadded new data successfully.")
            file.seek(0)
            updated_content= file.read()
            print("\nUpdated Content of the File:")
            print(updated_content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = "Test_r_plus.txt"
content= "\nThis line is appended using 'r+' mode."

with open(filename, 'w') as file:
    file.write("This is the original content of the file.")
read_and_write_file(filename, content)


def w_r_file(filename, content1):
    try:
        with open(filename, 'w+') as file:
            file.write(content1)
            print(f"data written to the file '{filename}'.")
            file.seek(0)
            added_data = file.read()
            print("\nContent of the file after writing:")
            print(added_data)
    except Exception as e:
        print(f"An error occurred: {e}")
filename = "Test_r_w_plus.txt"
content1 = """learning python is curious and having fun
and i like this learning process."""
w_r_file(filename, content1)

def append_r_file(filename, content2):
    try:
        with open(filename, 'a+') as file:
            file.write(content2)
            print(f"data added to the file '{filename}'.")
            file.seek(0)
            print("\ndata after appending:")
            print(file.read())
    except Exception as e:
        print(f"An error occurred: {e}")
filename = "Test_a_plus.txt"
content2= "\nThis line is added using 'a+' mode."

append_r_file(filename, content2)






